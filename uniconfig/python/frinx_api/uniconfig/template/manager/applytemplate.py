# generated by datamodel-codegen:
#   filename:  uniconfigV3.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from ...frinx import types


class TypedLeafValue(BaseModel):
    class Config:
        allow_population_by_field_name = True

    type: Optional[str] = None
    """
    Type qualifier for this value.
    Used in case the same variable is used under different types
    """
    leaf_value: str = Field(..., alias='leaf-value')
    """
    Value that can be applied to leaf.
    """
    leaf_list_values: list[str] = Field(..., alias='leaf-list-values')
    """
    List of values that can be applied to the leaf-list.
    """


class VariableItem(BaseModel):
    class Config:
        allow_population_by_field_name = True

    leaf_list_values: list[str] = Field(..., alias='leaf-list-values')
    """
    List of values that can be applied to the leaf-list.
    """
    typed_leaf_values: list[TypedLeafValue] = Field(..., alias='typed-leaf-values')
    leaf_value: str = Field(..., alias='leaf-value')
    """
    Value that can be applied to leaf.
    """
    variable_id: Optional[str] = Field(None, alias='variable-id')
    """
    Variable identifier.
    """


class UniconfigNodeItem(BaseModel):
    class Config:
        allow_population_by_field_name = True

    uniconfig_node_id: Optional[str] = Field(None, alias='uniconfig-node-id')
    """
    Identifier of the target Uniconfig node.
    """
    variable: Optional[list[VariableItem]] = None
    """
    List of variables with associated values.
    """


class Input(BaseModel):
    class Config:
        allow_population_by_field_name = True

    template_node_id: str = Field(..., alias='template-node-id')
    """
    Identifier of the template.
    """
    uniconfig_node: Optional[list[UniconfigNodeItem]] = Field(
        None, alias='uniconfig-node'
    )


class NodeResultItem(BaseModel):
    class Config:
        allow_population_by_field_name = True

    node_id: Optional[str] = Field(None, alias='node-id')
    error_type: Optional[types.ErrorType] = Field(None, alias='error-type')
    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Error message describing cause of error.
    """
    status: types.OperationResultType


class Output(BaseModel):
    class Config:
        allow_population_by_field_name = True

    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Error message that describe overall problem.
    """
    node_result: Optional[list[NodeResultItem]] = Field(None, alias='node-result')
    """
    RPC results per target Uniconfig node to which template is applied.
    """
    overall_status: types.OperationResultType = Field(..., alias='overall-status')