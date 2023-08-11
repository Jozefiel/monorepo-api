from __future__ import annotations

import typing

from pydantic import Field

from graphql_pydantic_converter.graphql_types import ENUM
from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.graphql_types import Interface
from graphql_pydantic_converter.graphql_types import Payload
from graphql_pydantic_converter.graphql_types import Query

ID: typing.TypeAlias = str
Int: typing.TypeAlias = int
String: typing.TypeAlias = str
Float: typing.TypeAlias = float
Boolean: typing.TypeAlias = bool


class NodeStatus(ENUM):
    ok = 'ok'
    unknown = 'unknown'


class NetRoutingPathOutputCollections(ENUM):
    NetDevice = 'NetDevice'
    NetInterface = 'NetInterface'


class __TypeKind(ENUM):
    SCALAR = 'SCALAR'
    OBJECT = 'OBJECT'
    INTERFACE = 'INTERFACE'
    UNION = 'UNION'
    ENUM = 'ENUM'
    INPUT_OBJECT = 'INPUT_OBJECT'
    LIST = 'LIST'
    NON_NULL = 'NON_NULL'


class __DirectiveLocation(ENUM):
    QUERY = 'QUERY'
    MUTATION = 'MUTATION'
    SUBSCRIPTION = 'SUBSCRIPTION'
    FIELD = 'FIELD'
    FRAGMENT_DEFINITION = 'FRAGMENT_DEFINITION'
    FRAGMENT_SPREAD = 'FRAGMENT_SPREAD'
    INLINE_FRAGMENT = 'INLINE_FRAGMENT'
    VARIABLE_DEFINITION = 'VARIABLE_DEFINITION'
    SCHEMA = 'SCHEMA'
    SCALAR = 'SCALAR'
    OBJECT = 'OBJECT'
    FIELD_DEFINITION = 'FIELD_DEFINITION'
    ARGUMENT_DEFINITION = 'ARGUMENT_DEFINITION'
    INTERFACE = 'INTERFACE'
    UNION = 'UNION'
    ENUM = 'ENUM'
    ENUM_VALUE = 'ENUM_VALUE'
    INPUT_OBJECT = 'INPUT_OBJECT'
    INPUT_FIELD_DEFINITION = 'INPUT_FIELD_DEFINITION'


class Node(Interface):
    id: typing.Optional[Boolean]


class NetDeviceFilter(Input):
    ospf_area_id: typing.Optional[String] = Field(alias='ospfAreaId')
    router_id: typing.Optional[String] = Field(alias='routerId')


class NetInterfaceFilter(Input):
    ip_address: typing.Optional[String] = Field(alias='ipAddress')


class NetNetworkFilter(Input):
    subnet: typing.Optional[String]
    ospf_route_type: typing.Optional[Int] = Field(alias='ospfRouteType')


class PhyDeviceFilter(Input):
    label: typing.Optional[String]
    name: typing.Optional[String]


class PhyInterfaceFilter(Input):
    status: typing.Optional[String]
    name: typing.Optional[String]


class NodeQuery(Query):
    _name: str = Field('node', const=True)
    id: ID
    payload: Node


class PhyDevicesQuery(Query):
    _name: str = Field('phyDevices', const=True)
    filter: typing.Optional[PhyDeviceFilter]
    first: Int
    cursor: typing.Optional[String]
    payload: PhyDeviceConnection


class NetDevicesQuery(Query):
    _name: str = Field('netDevices', const=True)
    filter: typing.Optional[NetDeviceFilter]
    first: Int
    cursor: typing.Optional[String]
    payload: NetDeviceConnection


class NetRoutingPathsQuery(Query):
    _name: str = Field('netRoutingPaths', const=True)
    device_from: ID = Field(alias='deviceFrom')
    device_to: ID = Field(alias='deviceTo')
    output_collection: typing.Optional[NetRoutingPathOutputCollections] = Field(alias='outputCollection')
    payload: NetRoutingPathConnection


class Coordinates(Payload):
    x: typing.Optional[Boolean] = Field(response='Float', default=True)
    y: typing.Optional[Boolean] = Field(response='Float', default=True)


class NetDevice(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    router_id: typing.Optional[Boolean] = Field(response='String', alias='routerId', default=True)
    ospf_area_id: typing.Optional[Boolean] = Field(response='String', alias='ospfAreaId', default=True)
    phy_device: typing.Optional[PhyDevice] = Field(response='PhyDevice', alias='phyDevice')
    net_networks: typing.Optional[NetNetworkConnection] = Field(response='NetNetworkConnection', alias='netNetworks')
    net_interfaces: typing.Optional[NetInterfaceConnection] = Field(response='NetInterfaceConnection', alias='netInterfaces')


class NetDeviceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(response='String', default=True)
    node: typing.Optional[NetDevice] = Field(response='NetDevice')


class NetDeviceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    edges: typing.Optional[NetDeviceEdge] = Field(response='NetDeviceEdge')


class NetInterface(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    ip_address: typing.Optional[Boolean] = Field(response='String', alias='ipAddress', default=True)
    net_device: typing.Optional[NetDevice] = Field(response='NetDevice', alias='netDevice')
    net_link: typing.Optional[NetInterface] = Field(response='NetInterface', alias='netLink')


class NetInterfaceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(response='String', default=True)
    node: typing.Optional[NetInterface] = Field(response='NetInterface')


class NetInterfaceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    edges: typing.Optional[NetInterfaceEdge] = Field(response='NetInterfaceEdge')


class NetNetwork(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    subnet: typing.Optional[Boolean] = Field(response='String', default=True)
    ospf_route_type: typing.Optional[Boolean] = Field(response='Int', alias='ospfRouteType', default=True)
    coordinates: typing.Optional[Coordinates] = Field(response='Coordinates')


class NetNetworkEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(response='String', default=True)
    node: typing.Optional[NetNetwork] = Field(response='NetNetwork')


class NetNetworkConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    edges: typing.Optional[NetNetworkEdge] = Field(response='NetNetworkEdge')


class ShortestPath(Payload):
    edges: typing.Optional[Boolean] = Field(response='ID', default=True)


class AlternativePaths(Payload):
    edges: typing.Optional[Boolean] = Field(response='ID', default=True)


class NetRoutingPathConnection(Payload):
    shortest_path: typing.Optional[ShortestPath] = Field(response='ShortestPath', alias='shortestPath')
    alternative_paths: typing.Optional[AlternativePaths] = Field(response='AlternativePaths', alias='alternativePaths')


class PageInfo(Payload):
    has_next_page: typing.Optional[Boolean] = Field(response='Boolean', alias='hasNextPage', default=True)
    end_cursor: typing.Optional[Boolean] = Field(response='String', alias='endCursor', default=True)


class PhyDevice(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    router_id: typing.Optional[Boolean] = Field(response='String', alias='routerId', default=True)
    coordinates: typing.Optional[Coordinates] = Field(response='Coordinates')
    details: typing.Optional[PhyDeviceDetails] = Field(response='PhyDeviceDetails')
    status: typing.Optional[Boolean] = Field(response='NodeStatus', default=True)
    labels: typing.Optional[Boolean] = Field(response='String', default=True)
    phy_interfaces: typing.Optional[PhyInterfaceConnection] = Field(response='PhyInterfaceConnection', alias='phyInterfaces')
    net_device: typing.Optional[NetDevice] = Field(response='NetDevice', alias='netDevice')


class PhyDeviceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(response='String', default=True)
    node: typing.Optional[PhyDevice] = Field(response='PhyDevice')


class PhyDeviceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    edges: typing.Optional[PhyDeviceEdge] = Field(response='PhyDeviceEdge')


class PhyDeviceDetails(Payload):
    device_type: typing.Optional[Boolean] = Field(response='String', default=True)
    sw_version: typing.Optional[Boolean] = Field(response='String', default=True)


class PhyInterface(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    status: typing.Optional[Boolean] = Field(response='String', default=True)
    phy_device: typing.Optional[PhyDevice] = Field(response='PhyDevice', alias='phyDevice')
    phy_link: typing.Optional[PhyInterface] = Field(response='PhyInterface', alias='phyLink')


class PhyInterfaceEdge(Payload):
    cursor: typing.Optional[Boolean] = Field(response='String', default=True)
    node: typing.Optional[PhyInterface] = Field(response='PhyInterface')


class PhyInterfaceConnection(Payload):
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    edges: typing.Optional[PhyInterfaceEdge] = Field(response='PhyInterfaceEdge')


class __Schema(Payload):
    description: typing.Optional[Boolean] = Field(response='String', default=True)
    types: typing.Optional[__Type] = Field(response='__Type')
    query_type: typing.Optional[__Type] = Field(response='__Type', alias='queryType')
    mutation_type: typing.Optional[__Type] = Field(response='__Type', alias='mutationType')
    subscription_type: typing.Optional[__Type] = Field(response='__Type', alias='subscriptionType')
    directives: typing.Optional[__Directive] = Field(response='__Directive')


class __Type(Payload):
    kind: typing.Optional[Boolean] = Field(response='__TypeKind', default=True)
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    description: typing.Optional[Boolean] = Field(response='String', default=True)
    specified_by_url: typing.Optional[Boolean] = Field(response='String', alias='specifiedByURL', default=True)
    fields: typing.Optional[__Field] = Field(response='__Field')
    interfaces: typing.Optional[__Type] = Field(response='__Type')
    possible_types: typing.Optional[__Type] = Field(response='__Type', alias='possibleTypes')
    enum_values: typing.Optional[__EnumValue] = Field(response='__EnumValue', alias='enumValues')
    input_fields: typing.Optional[__InputValue] = Field(response='__InputValue', alias='inputFields')
    of_type: typing.Optional[__Type] = Field(response='__Type', alias='ofType')


class __Field(Payload):
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    description: typing.Optional[Boolean] = Field(response='String', default=True)
    args: typing.Optional[__InputValue] = Field(response='__InputValue')
    type: typing.Optional[__Type] = Field(response='__Type')
    is_deprecated: typing.Optional[Boolean] = Field(response='Boolean', alias='isDeprecated', default=True)
    deprecation_reason: typing.Optional[Boolean] = Field(response='String', alias='deprecationReason', default=True)


class __InputValue(Payload):
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    description: typing.Optional[Boolean] = Field(response='String', default=True)
    type: typing.Optional[__Type] = Field(response='__Type')
    default_value: typing.Optional[Boolean] = Field(response='String', alias='defaultValue', default=True)
    is_deprecated: typing.Optional[Boolean] = Field(response='Boolean', alias='isDeprecated', default=True)
    deprecation_reason: typing.Optional[Boolean] = Field(response='String', alias='deprecationReason', default=True)


class __EnumValue(Payload):
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    description: typing.Optional[Boolean] = Field(response='String', default=True)
    is_deprecated: typing.Optional[Boolean] = Field(response='Boolean', alias='isDeprecated', default=True)
    deprecation_reason: typing.Optional[Boolean] = Field(response='String', alias='deprecationReason', default=True)


class __Directive(Payload):
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    description: typing.Optional[Boolean] = Field(response='String', default=True)
    is_repeatable: typing.Optional[Boolean] = Field(response='Boolean', alias='isRepeatable', default=True)
    locations: typing.Optional[Boolean] = Field(response='__DirectiveLocation', default=True)
    args: typing.Optional[__InputValue] = Field(response='__InputValue')


Node.update_forward_refs()
NetDeviceFilter.update_forward_refs()
NetInterfaceFilter.update_forward_refs()
NetNetworkFilter.update_forward_refs()
PhyDeviceFilter.update_forward_refs()
PhyInterfaceFilter.update_forward_refs()
NodeQuery.update_forward_refs()
PhyDevicesQuery.update_forward_refs()
NetDevicesQuery.update_forward_refs()
NetRoutingPathsQuery.update_forward_refs()
Coordinates.update_forward_refs()
NetDevice.update_forward_refs()
NetDeviceEdge.update_forward_refs()
NetDeviceConnection.update_forward_refs()
NetInterface.update_forward_refs()
NetInterfaceEdge.update_forward_refs()
NetInterfaceConnection.update_forward_refs()
NetNetwork.update_forward_refs()
NetNetworkEdge.update_forward_refs()
NetNetworkConnection.update_forward_refs()
ShortestPath.update_forward_refs()
AlternativePaths.update_forward_refs()
NetRoutingPathConnection.update_forward_refs()
PageInfo.update_forward_refs()
PhyDevice.update_forward_refs()
PhyDeviceEdge.update_forward_refs()
PhyDeviceConnection.update_forward_refs()
PhyDeviceDetails.update_forward_refs()
PhyInterface.update_forward_refs()
PhyInterfaceEdge.update_forward_refs()
PhyInterfaceConnection.update_forward_refs()
__Schema.update_forward_refs()
__Type.update_forward_refs()
__Field.update_forward_refs()
__InputValue.update_forward_refs()
__EnumValue.update_forward_refs()
__Directive.update_forward_refs()
