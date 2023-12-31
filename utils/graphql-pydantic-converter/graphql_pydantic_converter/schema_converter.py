from __future__ import annotations

import re
from enum import Enum
from string import Template
from typing import Any
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class GraphqlJsonParser:
    """
    A Graphql JSON schema to pydantic model converter.
    """

    __INDENT: str = '    '
    __items: dict[str, Any]
    __result: str = ''
    __enums: list[str] = []
    __refs: str = ''
    __refs_template: Template = Template('$class_name.update_forward_refs()\n')
    __class_template: Template = Template('\n\nclass ${name}($type):\n')
    __ignore_enums: list[str] = ['String', 'ID', 'Float', 'Int', 'Boolean', 'list']
    __input_json: dict[str, Any]

    class ConverterMap(str, Enum):
        OBJECT = 'Payload'
        INTERFACE = 'Interface'
        ENUM = 'ENUM'
        INPUT_OBJECT = 'Input'
        SUBSCRIPTION = 'Subscription'
        MUTATION = 'Mutation'
        QUERY = 'Query'

    class GraphqlType(str, Enum):
        QUERY = 'queryType'
        MUTATION = 'mutationType'
        SUBSCRIPTION = 'subscriptionType'

    class TypeKind(str, Enum):
        SCALAR = 'SCALAR'
        OBJECT = 'OBJECT'
        INTERFACE = 'INTERFACE'
        UNION = 'UNION'
        ENUM = 'ENUM'
        INPUT_OBJECT = 'INPUT_OBJECT'
        LIST = 'LIST'
        NON_NULL = 'NON_NULL'

    class Scalars(str, Enum):
        ID = 'ID'
        String = 'String'
        LIST = 'LIST'
        Float = 'Float'
        Int = 'Int'
        Boolean = 'Boolean'
        Upload = 'Upload'

    class QueryType(BaseModel):
        name: Optional[str]

    class MutationType(BaseModel):
        name: Optional[str]

    class SubscriptionType(BaseModel):
        name: Optional[str]

    class OfType(BaseModel):
        kind: Optional[GraphqlJsonParser.TypeKind]
        name: Optional[str]
        of_type: Optional[GraphqlJsonParser.OfType] = Field(alias='ofType')

    class OfTypeItem(BaseModel):
        kind: Optional[GraphqlJsonParser.TypeKind]
        name: Optional[str]
        of_type: Optional[GraphqlJsonParser.OfTypeItem] = Field(alias='ofType')

    class Arg(BaseModel):
        name: Optional[str]
        description: Optional[Any]
        type: Optional[GraphqlJsonParser.Type]
        default_value: Optional[str] = Field(alias='defaultValue')
        is_deprecated: Optional[bool] = Field(alias='isDeprecated')
        deprecation_reason: Optional[Any] = Field(alias='deprecationReason')

    class Field(BaseModel):
        name: Optional[str]
        description: Optional[str]
        args: Optional[list[GraphqlJsonParser.Arg]]
        type: Optional[GraphqlJsonParser.Type]
        is_deprecated: Optional[bool] = Field(alias='isDeprecated')
        deprecation_reason: Optional[Any] = Field(alias='deprecationReason')

    class InputField(BaseModel):
        name: Optional[str]
        description: Optional[Any]
        type: Optional[GraphqlJsonParser.Type]
        default_value: Optional[Any] = Field(alias='defaultValue')
        is_deprecated: Optional[bool] = Field(alias='isDeprecated')
        deprecation_reason: Optional[Any] = Field(alias='deprecationReason')

    class Interface(BaseModel):
        kind: Optional[GraphqlJsonParser.TypeKind]
        name: Optional[str]
        of_type: Optional[Any] = Field(alias='ofType')

    class EnumValue(BaseModel):
        name: Optional[str]
        description: Optional[str]
        is_deprecated: Optional[bool] = Field(alias='isDeprecated')
        deprecation_reason: Optional[Any] = Field(alias='deprecationReason')

    class PossibleType(BaseModel):
        kind: Optional[GraphqlJsonParser.TypeKind]
        name: Optional[str]
        of_type: Optional[Any] = Field(alias='ofType')

    class Type(BaseModel):
        kind: GraphqlJsonParser.TypeKind
        name: Optional[str]
        description: Optional[str]
        fields: Optional[list[GraphqlJsonParser.Field]]
        input_fields: Optional[list[GraphqlJsonParser.InputField]] = Field(alias='inputFields')
        interfaces: Optional[list[GraphqlJsonParser.Interface]]
        enum_values: Optional[list[GraphqlJsonParser.EnumValue]] = Field(alias='enumValues')
        possible_types: Optional[list[GraphqlJsonParser.PossibleType]] = Field(alias='possibleTypes')
        of_type: Optional[GraphqlJsonParser.OfType] = Field(alias='ofType')

    class Directive(BaseModel):
        name: Optional[str]
        description: Optional[str]
        is_repeatable: Optional[bool] = Field(alias='isRepeatable')
        locations: Optional[list[str]]
        args: Optional[list[GraphqlJsonParser.Arg]]

    class Model(BaseModel):
        query_type: Optional[GraphqlJsonParser.QueryType] = Field(default=None, alias='queryType')
        mutation_type: Optional[GraphqlJsonParser.MutationType] = Field(default=None, alias='mutationType')
        subscription_type: Optional[GraphqlJsonParser.SubscriptionType] = Field(default=None, alias='subscriptionType')
        types: Optional[list[GraphqlJsonParser.Type]] = Field(default=None)
        directives: Optional[list[GraphqlJsonParser.Directive]] = Field(default=None)

    class Schema(BaseModel):
        graphql_schema: Optional[GraphqlJsonParser.Model] = Field(alias='__schema')
        data: Optional[GraphqlJsonParser.Schema] = None

        class Config:
            allow_population_by_field_name = True

    def __init__(self, input_json: dict[str, Any]) -> None:
        self.__input_json = input_json
        self.__convert()

    def __convert(self) -> None:
        items: dict[str, Any] = {i: [] for i in self.TypeKind}

        schema = self.Schema(**self.__input_json)
        pydantic_data: Optional[GraphqlJsonParser.Model] = None

        if schema.graphql_schema:
            pydantic_data = schema.graphql_schema
        elif schema.data:
            if schema.data.graphql_schema:
                pydantic_data = schema.data.graphql_schema

        if not pydantic_data:
            raise Exception(
                'Invalid input format. The JSON schema must start with "data.__schema" or "__schema" at the root level.'
            )

        if pydantic_data.types:
            for item in pydantic_data.types:
                items[item.kind].append(item)

        worker_list = []
        if pydantic_data.query_type:
            worker_list.append(pydantic_data.query_type.name)
        if pydantic_data.mutation_type:
            worker_list.append(pydantic_data.mutation_type.name)
        if pydantic_data.subscription_type:
            worker_list.append(pydantic_data.subscription_type.name)

        self.__import_classes(items, worker_list)
        self.__create_scalar(items[self.TypeKind.SCALAR])
        self.__create_enum(items[self.TypeKind.ENUM])
        self.__create_interface(items[GraphqlJsonParser.TypeKind.INTERFACE])
        self.__create_input(items[GraphqlJsonParser.TypeKind.INPUT_OBJECT])
        self.__create_payload(items[GraphqlJsonParser.TypeKind.OBJECT], worker_list)
        self.__create_refs()

    def __import_classes(self, items: dict[str, Any], worker_list: list[Optional[str]]) -> None:
        kv_template = Template('from graphql_pydantic_converter.graphql_types import $type\n')

        imports = [
            'from __future__ import annotations\n\n'
            'import typing\n',
            'from pydantic import Field',
            '\n'
        ]
        self.__result += '\n'.join(imports)

        if items[GraphqlJsonParser.TypeKind.ENUM]:
            self.__result += kv_template.substitute(type=GraphqlJsonParser.ConverterMap.ENUM.value)
        if items[GraphqlJsonParser.TypeKind.INPUT_OBJECT]:
            self.__result += kv_template.substitute(type=GraphqlJsonParser.ConverterMap.INPUT_OBJECT.value)
        if items[GraphqlJsonParser.TypeKind.INTERFACE]:
            self.__result += kv_template.substitute(type=GraphqlJsonParser.ConverterMap.INTERFACE.value)
        if GraphqlJsonParser.ConverterMap.MUTATION in worker_list:
            self.__result += kv_template.substitute(type=GraphqlJsonParser.ConverterMap.MUTATION.value)
        if items[GraphqlJsonParser.TypeKind.OBJECT]:
            self.__result += kv_template.substitute(type=GraphqlJsonParser.ConverterMap.OBJECT.value)
        if GraphqlJsonParser.ConverterMap.QUERY in worker_list:
            self.__result += kv_template.substitute(type=GraphqlJsonParser.ConverterMap.QUERY.value)
        if GraphqlJsonParser.ConverterMap.SUBSCRIPTION in worker_list:
            self.__result += kv_template.substitute(type=GraphqlJsonParser.ConverterMap.SUBSCRIPTION.value)
        self.__result += '\n'

    def __extract_fields(self, of_type: OfType | Type, previous: list[Any]) -> list[Any]:
        if of_type.of_type is None:
            previous.append(of_type.name)
            return previous
        else:
            previous.append(of_type.kind)
            self.__extract_fields(of_type.of_type, previous)
            return previous

    @staticmethod
    def __build_type(fields: list[Any]) -> Any:
        rendered_type = fields[-1]
        optional_count = 0

        if len(fields) == 1 and fields[0] not in ['NON_NULL', 'LIST']:
            return f'typing.Optional[{rendered_type}]'

        for item in reversed(fields):
            if item not in ['NON_NULL', 'LIST']:
                continue
            elif item == 'NON_NULL':
                rendered_type = f'{rendered_type}'
            elif item == 'LIST':
                rendered_type = f'list[{rendered_type}]'
                optional_count += 1

        if optional_count > 0:
            rendered_type = f'typing.Optional[{rendered_type}]'
        return rendered_type

    @staticmethod
    def __build_type_payload(fields: list[Any]) -> Any:
        rendered_type = fields[-1]
        optional_count = 0

        if len(fields) == 1 and fields[0] not in ['NON_NULL', 'LIST']:
            return f'{rendered_type}'

        for item in reversed(fields):
            if item not in ['NON_NULL', 'LIST']:
                continue
            elif item == 'NON_NULL':
                rendered_type = f'{rendered_type}'
            elif item == 'LIST':
                rendered_type = f'{rendered_type}'
                optional_count += 1

        if optional_count > 0:
            rendered_type = f'{rendered_type}'
        return rendered_type

    @staticmethod
    def is_not_snake_case(string: str) -> bool:
        pattern = r'^[a-z]+(_[a-z]+)*$'  # Pattern for snake_case
        return not re.match(pattern, string)

    @staticmethod
    def to_snake_case(string: str) -> str:
        snake_case = re.sub(r'([A-Z]+)', r'_\1', string).lower()
        snake_case = re.sub(r'\W+', '_', snake_case).strip('_')
        return snake_case

    def __create_scalar(self, scalars: list[Type]) -> None:
        kv_template = Template('$name: typing.TypeAlias = $type\n')
        for scalar in scalars:
            if scalar.name:
                scalar_type = 'typing.Any'
                match scalar.name:
                    case self.Scalars.String:
                        scalar_type = 'str'
                    case self.Scalars.Boolean:
                        scalar_type = 'bool'
                    case self.Scalars.Int:
                        scalar_type = 'int'
                    case self.Scalars.Float:
                        scalar_type = 'float'
                    case self.Scalars.LIST:
                        scalar_type = 'list'
                    case self.Scalars.ID:
                        scalar_type = 'str'
                self.__result += kv_template.substitute(indent=self.__INDENT, name=scalar.name, type=scalar_type)
                self.__ignore_enums.append(scalar.name)

    def __create_enum(self, enums: list[Type]) -> None:
        kv_template = Template("$indent$name = '$name'\n")
        for enum in enums:
            tmp_enum = [self.__class_template.substitute(name=enum.name, type='ENUM')]
            if enum.enum_values:
                for i in enum.enum_values:
                    tmp_enum.append(kv_template.substitute(indent=self.__INDENT, name=i.name))
                self.__result += (''.join(tmp_enum))
                if enum.name:
                    self.__enums.append(enum.name)

    def __create_interface(self, interfaces: list[Type]) -> None:
        enums = self.__enums + self.__ignore_enums
        kv_template = Template('$indent$name: $val$alias\n')
        for interface in interfaces:
            self.__result += self.__class_template.substitute(name=interface.name, type='Interface')
            self.__refs += self.__refs_template.substitute(class_name=interface.name)
            if interface.fields:
                for field in interface.fields:
                    if field.name and field.type:
                        name = field.name
                        alias = ''
                        if self.is_not_snake_case(field.name):
                            alias = f" = Field(alias='{field.name}')"
                            name = self.to_snake_case(field.name)

                        kind = self.__build_type_payload(self.__extract_fields(field.type, []))
                        val = f'typing.Optional[{kind}]'
                        if kind in enums:
                            val = 'typing.Optional[Boolean]'
                        self.__result += kv_template.substitute(
                            indent=self.__INDENT, name=name, val=val, alias=alias
                        )

    def __create_input(self, inputs: list[Type]) -> None:
        kv_template = Template('$indent$name: $val$alias\n')
        for _input in inputs:
            self.__result += self.__class_template.substitute(name=_input.name, type='Input')
            self.__refs += self.__refs_template.substitute(class_name=_input.name)
            if _input.input_fields:
                for field in _input.input_fields:
                    if field.name and field.type:
                        name = field.name
                        alias = ''
                        if self.is_not_snake_case(field.name):
                            alias = f" = Field(alias='{field.name}')"
                            name = self.to_snake_case(field.name)

                        kind = self.__build_type(self.__extract_fields(field.type, []))
                        self.__result += kv_template.substitute(
                            indent=self.__INDENT, name=name, val=kind, alias=alias
                        )

    def __create_object_payload(self, payload: Type) -> None:
        kv_template = Template('$indent$name: $val = Field(response=$type)\n')

        interface = ''
        if payload.interfaces:
            for i in payload.interfaces:
                interface += f', {i.name}'

        self.__result += self.__class_template.substitute(name=payload.name, type='Payload')
        self.__refs += self.__refs_template.substitute(class_name=payload.name)

        if payload.fields:
            for field in payload.fields:
                if field.name and field.type:
                    name = field.name
                    kind = self.__build_type_payload(self.__extract_fields(field.type, []))
                    val = f'typing.Optional[{kind}]'
                    val_type = f"'{kind}'"
                    if self.is_not_snake_case(field.name):
                        val_type += f", alias='{field.name}'"
                        name = self.to_snake_case(field.name)

                    if kind in (self.__enums + self.__ignore_enums):
                        val = 'typing.Optional[Boolean]'
                        val_type += ', default=True'
                    self.__result += kv_template.substitute(
                        indent=self.__INDENT, name=name, val=val, type=val_type
                    )

    def __create_specific_payload(self, payload: Type) -> None:
        kv_template = Template('$indent$name: $val\n')

        interface = ''
        enums = self.__enums + self.__ignore_enums

        if payload.interfaces:
            for i in payload.interfaces:
                interface += f', {i.name}'
        if payload.fields and payload.name:
            for field in payload.fields:
                if field.name and field.type:
                    self.__result += self.__class_template.substitute(
                        name=field.name[0].upper() + field.name[1:] + payload.name,
                        type=payload.name + interface,
                    )

                    self.__result += f"{self.__INDENT}_name: str = Field('{field.name}', const=True)\n"
                    self.__refs += self.__refs_template.substitute(
                        class_name=field.name[0].upper() + field.name[1:] + payload.name
                    )
                    if field.args:
                        for arg in field.args:
                            if arg.type and arg.name:
                                kind = self.__build_type(self.__extract_fields(arg.type, []))
                                name = arg.name
                                if self.is_not_snake_case(arg.name):
                                    kind += f" = Field(alias='{arg.name}')"
                                    name = self.to_snake_case(arg.name)
                                self.__result += kv_template.substitute(indent=self.__INDENT, name=name, val=kind)
                        kind = self.__build_type_payload(self.__extract_fields(field.type, []))
                        if kind in enums:
                            self.__result += kv_template.substitute(indent=self.__INDENT, name='payload', val='Boolean')
                        else:
                            self.__result += kv_template.substitute(indent=self.__INDENT, name='payload', val=kind)

    def __create_payload(self, payloads: list[Type], specific_payloads: list[Optional[str]]) -> None:
        for payload in payloads:
            if payload.name in specific_payloads:
                self.__create_specific_payload(payload)
            else:
                self.__create_object_payload(payload)

    def __create_refs(self) -> None:
        self.__result += f'\n\n{self.__refs}'

    def render(self) -> str:
        return self.__result

    def export(self, output_file: str) -> None:
        output = open(output_file, 'w')
        output.write(self.__result)
        output.close()


GraphqlJsonParser.Schema.update_forward_refs()
GraphqlJsonParser.Model.update_forward_refs()
GraphqlJsonParser.InputField.update_forward_refs()
GraphqlJsonParser.Field.update_forward_refs()
GraphqlJsonParser.Arg.update_forward_refs()
GraphqlJsonParser.Type.update_forward_refs()
GraphqlJsonParser.OfType.update_forward_refs()
GraphqlJsonParser.OfTypeItem.update_forward_refs()
GraphqlJsonParser.PossibleType.update_forward_refs()
GraphqlJsonParser.Interface.update_forward_refs()
GraphqlJsonParser.Directive.update_forward_refs()
