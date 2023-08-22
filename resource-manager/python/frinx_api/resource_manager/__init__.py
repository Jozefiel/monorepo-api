from __future__ import annotations

import typing

from graphql_pydantic_converter.graphql_types import ENUM
from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.graphql_types import Interface
from graphql_pydantic_converter.graphql_types import Mutation
from graphql_pydantic_converter.graphql_types import Payload
from graphql_pydantic_converter.graphql_types import Query
from pydantic import Field

Boolean: typing.TypeAlias = bool
Cursor: typing.TypeAlias = typing.Any
Float: typing.TypeAlias = float
ID: typing.TypeAlias = str
Int: typing.TypeAlias = int
Map: typing.TypeAlias = typing.Any
String: typing.TypeAlias = str


class AllocationStrategyLang(ENUM):
    js = 'js'
    py = 'py'


class PoolType(ENUM):
    allocating = 'allocating'
    set = 'set'
    singleton = 'singleton'


class Node(Interface):
    id: typing.Optional[Boolean]


class CreateAllocatingPoolInput(Input):
    allocation_strategy_id: ID = Field(alias='allocationStrategyId')
    description: typing.Optional[String]
    pool_dealocation_safety_period: Int = Field(alias='poolDealocationSafetyPeriod')
    pool_name: String = Field(alias='poolName')
    pool_properties: Map = Field(alias='poolProperties')
    pool_property_types: Map = Field(alias='poolPropertyTypes')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]]


class CreateAllocationStrategyInput(Input):
    name: String
    description: typing.Optional[String]
    script: String
    lang: AllocationStrategyLang
    expected_pool_property_types: typing.Optional[Map] = Field(alias='expectedPoolPropertyTypes')


class CreateNestedAllocatingPoolInput(Input):
    allocation_strategy_id: ID = Field(alias='allocationStrategyId')
    description: typing.Optional[String]
    parent_resource_id: ID = Field(alias='parentResourceId')
    pool_dealocation_safety_period: Int = Field(alias='poolDealocationSafetyPeriod')
    pool_name: String = Field(alias='poolName')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]]


class CreateNestedSetPoolInput(Input):
    description: typing.Optional[String]
    parent_resource_id: ID = Field(alias='parentResourceId')
    pool_dealocation_safety_period: Int = Field(alias='poolDealocationSafetyPeriod')
    pool_name: String = Field(alias='poolName')
    pool_values: typing.Optional[list[Map]] = Field(alias='poolValues')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]]


class CreateNestedSingletonPoolInput(Input):
    description: typing.Optional[String]
    parent_resource_id: ID = Field(alias='parentResourceId')
    pool_name: String = Field(alias='poolName')
    pool_values: typing.Optional[list[Map]] = Field(alias='poolValues')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]]


class CreateResourceTypeInput(Input):
    resource_name: String = Field(alias='resourceName')
    resource_properties: Map = Field(alias='resourceProperties')


class CreateSetPoolInput(Input):
    description: typing.Optional[String]
    pool_dealocation_safety_period: Int = Field(alias='poolDealocationSafetyPeriod')
    pool_name: String = Field(alias='poolName')
    pool_values: typing.Optional[list[Map]] = Field(alias='poolValues')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]]


class CreateSingletonPoolInput(Input):
    description: typing.Optional[String]
    pool_name: String = Field(alias='poolName')
    pool_values: typing.Optional[list[Map]] = Field(alias='poolValues')
    resource_type_id: ID = Field(alias='resourceTypeId')
    tags: typing.Optional[list[String]]


class CreateTagInput(Input):
    tag_text: String = Field(alias='tagText')


class DeleteAllocationStrategyInput(Input):
    allocation_strategy_id: ID = Field(alias='allocationStrategyId')


class DeleteResourcePoolInput(Input):
    resource_pool_id: ID = Field(alias='resourcePoolId')


class DeleteResourceTypeInput(Input):
    resource_type_id: ID = Field(alias='resourceTypeId')


class DeleteTagInput(Input):
    tag_id: ID = Field(alias='tagId')


class ResourceInput(Input):
    properties: Map = Field(alias='Properties')
    status: String = Field(alias='Status')
    updated_at: String = Field(alias='UpdatedAt')


class ResourcePoolInput(Input):
    resource_pool_id: ID = Field(alias='ResourcePoolID')
    resource_pool_name: String = Field(alias='ResourcePoolName')
    pool_properties: Map = Field(alias='poolProperties')


class TagAnd(Input):
    matches_all: typing.Optional[list[String]] = Field(alias='matchesAll')


class TagOr(Input):
    matches_any: typing.Optional[list[TagAnd]] = Field(alias='matchesAny')


class TagPoolInput(Input):
    tag_id: ID = Field(alias='tagId')
    pool_id: ID = Field(alias='poolId')


class UntagPoolInput(Input):
    tag_id: ID = Field(alias='tagId')
    pool_id: ID = Field(alias='poolId')


class UpdateResourceTypeNameInput(Input):
    resource_type_id: ID = Field(alias='resourceTypeId')
    resource_name: String = Field(alias='resourceName')


class UpdateTagInput(Input):
    tag_id: ID = Field(alias='tagId')
    tag_text: String = Field(alias='tagText')


class AllocationStrategy(Payload):
    description: typing.Optional[Boolean] = Field(response='String', alias='Description', default=True)
    lang: typing.Optional[Boolean] = Field(response='AllocationStrategyLang', alias='Lang', default=True)
    name: typing.Optional[Boolean] = Field(response='String', alias='Name', default=True)
    script: typing.Optional[Boolean] = Field(response='String', alias='Script', default=True)
    id: typing.Optional[Boolean] = Field(response='ID', default=True)


class CreateAllocatingPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class CreateAllocationStrategyPayload(Payload):
    strategy: typing.Optional[AllocationStrategy] = Field(response='AllocationStrategy')


class CreateNestedAllocatingPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class CreateNestedSetPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class CreateNestedSingletonPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class CreateResourceTypePayload(Payload):
    resource_type: typing.Optional[ResourceType] = Field(response='ResourceType', alias='resourceType')


class CreateSetPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class CreateSingletonPoolPayload(Payload):
    pool: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class CreateTagPayload(Payload):
    tag: typing.Optional[Tag] = Field(response='Tag')


class DeleteAllocationStrategyPayload(Payload):
    strategy: typing.Optional[AllocationStrategy] = Field(response='AllocationStrategy')


class DeleteResourcePoolPayload(Payload):
    resource_pool_id: typing.Optional[Boolean] = Field(response='ID', alias='resourcePoolId', default=True)


class DeleteResourceTypePayload(Payload):
    resource_type_id: typing.Optional[Boolean] = Field(response='ID', alias='resourceTypeId', default=True)


class DeleteTagPayload(Payload):
    tag_id: typing.Optional[Boolean] = Field(response='ID', alias='tagId', default=True)


class CreateTagMutation(Mutation):
    _name: str = Field('CreateTag', const=True)
    input: CreateTagInput
    payload: CreateTagPayload


class UpdateTagMutation(Mutation):
    _name: str = Field('UpdateTag', const=True)
    input: UpdateTagInput
    payload: UpdateTagPayload


class DeleteTagMutation(Mutation):
    _name: str = Field('DeleteTag', const=True)
    input: DeleteTagInput
    payload: DeleteTagPayload


class TagPoolMutation(Mutation):
    _name: str = Field('TagPool', const=True)
    input: TagPoolInput
    payload: TagPoolPayload


class UntagPoolMutation(Mutation):
    _name: str = Field('UntagPool', const=True)
    input: UntagPoolInput
    payload: UntagPoolPayload


class CreateAllocationStrategyMutation(Mutation):
    _name: str = Field('CreateAllocationStrategy', const=True)
    input: typing.Optional[CreateAllocationStrategyInput]
    payload: CreateAllocationStrategyPayload


class DeleteAllocationStrategyMutation(Mutation):
    _name: str = Field('DeleteAllocationStrategy', const=True)
    input: typing.Optional[DeleteAllocationStrategyInput]
    payload: DeleteAllocationStrategyPayload


class TestAllocationStrategyMutation(Mutation):
    _name: str = Field('TestAllocationStrategy', const=True)
    allocation_strategy_id: ID = Field(alias='allocationStrategyId')
    resource_pool: ResourcePoolInput = Field(alias='resourcePool')
    current_resources: typing.Optional[list[ResourceInput]] = Field(alias='currentResources')
    user_input: Map = Field(alias='userInput')
    payload: Boolean


class ClaimResourceMutation(Mutation):
    _name: str = Field('ClaimResource', const=True)
    pool_id: ID = Field(alias='poolId')
    description: typing.Optional[String]
    user_input: Map = Field(alias='userInput')
    payload: Resource


class ClaimResourceWithAltIdMutation(Mutation):
    _name: str = Field('ClaimResourceWithAltId', const=True)
    pool_id: ID = Field(alias='poolId')
    description: typing.Optional[String]
    user_input: Map = Field(alias='userInput')
    alternative_id: Map = Field(alias='alternativeId')
    payload: Resource


class FreeResourceMutation(Mutation):
    _name: str = Field('FreeResource', const=True)
    input: Map
    pool_id: ID = Field(alias='poolId')
    payload: Boolean


class CreateSetPoolMutation(Mutation):
    _name: str = Field('CreateSetPool', const=True)
    input: CreateSetPoolInput
    payload: CreateSetPoolPayload


class CreateNestedSetPoolMutation(Mutation):
    _name: str = Field('CreateNestedSetPool', const=True)
    input: CreateNestedSetPoolInput
    payload: CreateNestedSetPoolPayload


class CreateSingletonPoolMutation(Mutation):
    _name: str = Field('CreateSingletonPool', const=True)
    input: typing.Optional[CreateSingletonPoolInput]
    payload: CreateSingletonPoolPayload


class CreateNestedSingletonPoolMutation(Mutation):
    _name: str = Field('CreateNestedSingletonPool', const=True)
    input: CreateNestedSingletonPoolInput
    payload: CreateNestedSingletonPoolPayload


class CreateAllocatingPoolMutation(Mutation):
    _name: str = Field('CreateAllocatingPool', const=True)
    input: typing.Optional[CreateAllocatingPoolInput]
    payload: CreateAllocatingPoolPayload


class CreateNestedAllocatingPoolMutation(Mutation):
    _name: str = Field('CreateNestedAllocatingPool', const=True)
    input: CreateNestedAllocatingPoolInput
    payload: CreateNestedAllocatingPoolPayload


class DeleteResourcePoolMutation(Mutation):
    _name: str = Field('DeleteResourcePool', const=True)
    input: DeleteResourcePoolInput
    payload: DeleteResourcePoolPayload


class CreateResourceTypeMutation(Mutation):
    _name: str = Field('CreateResourceType', const=True)
    input: CreateResourceTypeInput
    payload: CreateResourceTypePayload


class DeleteResourceTypeMutation(Mutation):
    _name: str = Field('DeleteResourceType', const=True)
    input: DeleteResourceTypeInput
    payload: DeleteResourceTypePayload


class UpdateResourceTypeNameMutation(Mutation):
    _name: str = Field('UpdateResourceTypeName', const=True)
    input: UpdateResourceTypeNameInput
    payload: UpdateResourceTypeNamePayload


class UpdateResourceAltIdMutation(Mutation):
    _name: str = Field('UpdateResourceAltId', const=True)
    input: Map
    pool_id: ID = Field(alias='poolId')
    alternative_id: Map = Field(alias='alternativeId')
    payload: Resource


class OutputCursor(Payload):
    id: typing.Optional[Boolean] = Field(response='String', alias='ID', default=True)


class PageInfo(Payload):
    end_cursor: typing.Optional[OutputCursor] = Field(response='OutputCursor', alias='endCursor')
    has_next_page: typing.Optional[Boolean] = Field(response='Boolean', alias='hasNextPage', default=True)
    has_previous_page: typing.Optional[Boolean] = Field(response='Boolean', alias='hasPreviousPage', default=True)
    start_cursor: typing.Optional[OutputCursor] = Field(response='OutputCursor', alias='startCursor')


class PoolCapacityPayload(Payload):
    free_capacity: typing.Optional[Boolean] = Field(response='String', alias='freeCapacity', default=True)
    utilized_capacity: typing.Optional[Boolean] = Field(response='String', alias='utilizedCapacity', default=True)


class PropertyType(Payload):
    float_val: typing.Optional[Boolean] = Field(response='Float', alias='FloatVal', default=True)
    int_val: typing.Optional[Boolean] = Field(response='Int', alias='IntVal', default=True)
    mandatory: typing.Optional[Boolean] = Field(response='Boolean', alias='Mandatory', default=True)
    string_val: typing.Optional[Boolean] = Field(response='String', alias='StringVal', default=True)
    name: typing.Optional[Boolean] = Field(response='String', alias='Name', default=True)
    type: typing.Optional[Boolean] = Field(response='String', alias='Type', default=True)
    id: typing.Optional[Boolean] = Field(response='ID', default=True)


class QueryPoolCapacityQuery(Query):
    _name: str = Field('QueryPoolCapacity', const=True)
    pool_id: ID = Field(alias='poolId')
    payload: PoolCapacityPayload


class QueryPoolTypesQuery(Query):
    _name: str = Field('QueryPoolTypes', const=True)


class QueryResourceQuery(Query):
    _name: str = Field('QueryResource', const=True)
    input: Map
    pool_id: ID = Field(alias='poolId')
    payload: Resource


class QueryResourcesQuery(Query):
    _name: str = Field('QueryResources', const=True)
    pool_id: ID = Field(alias='poolId')
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[String]
    after: typing.Optional[String]
    payload: ResourceConnection


class QueryResourcesByAltIdQuery(Query):
    _name: str = Field('QueryResourcesByAltId', const=True)
    input: Map
    pool_id: typing.Optional[ID] = Field(alias='poolId')
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[String]
    after: typing.Optional[String]
    payload: ResourceConnection


class QueryAllocationStrategyQuery(Query):
    _name: str = Field('QueryAllocationStrategy', const=True)
    allocation_strategy_id: ID = Field(alias='allocationStrategyId')
    payload: AllocationStrategy


class QueryAllocationStrategiesQuery(Query):
    _name: str = Field('QueryAllocationStrategies', const=True)
    by_name: typing.Optional[String] = Field(alias='byName')
    payload: AllocationStrategy


class QueryResourceTypesQuery(Query):
    _name: str = Field('QueryResourceTypes', const=True)
    by_name: typing.Optional[String] = Field(alias='byName')
    payload: ResourceType


class QueryRequiredPoolPropertiesQuery(Query):
    _name: str = Field('QueryRequiredPoolProperties', const=True)
    allocation_strategy_name: String = Field(alias='allocationStrategyName')
    payload: PropertyType


class QueryResourcePoolQuery(Query):
    _name: str = Field('QueryResourcePool', const=True)
    pool_id: ID = Field(alias='poolId')
    payload: ResourcePool


class QueryEmptyResourcePoolsQuery(Query):
    _name: str = Field('QueryEmptyResourcePools', const=True)
    resource_type_id: typing.Optional[ID] = Field(alias='resourceTypeId')
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[Cursor]
    after: typing.Optional[Cursor]
    payload: ResourcePoolConnection


class QueryResourcePoolsQuery(Query):
    _name: str = Field('QueryResourcePools', const=True)
    resource_type_id: typing.Optional[ID] = Field(alias='resourceTypeId')
    tags: typing.Optional[TagOr]
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[Cursor]
    after: typing.Optional[Cursor]
    filter_by_resources: typing.Optional[Map] = Field(alias='filterByResources')
    payload: ResourcePoolConnection


class QueryRecentlyActiveResourcesQuery(Query):
    _name: str = Field('QueryRecentlyActiveResources', const=True)
    from_datetime: String = Field(alias='fromDatetime')
    to_datetime: typing.Optional[String] = Field(alias='toDatetime')
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[String]
    after: typing.Optional[String]
    payload: ResourceConnection


class QueryResourcePoolHierarchyPathQuery(Query):
    _name: str = Field('QueryResourcePoolHierarchyPath', const=True)
    pool_id: ID = Field(alias='poolId')
    payload: ResourcePool


class QueryRootResourcePoolsQuery(Query):
    _name: str = Field('QueryRootResourcePools', const=True)
    resource_type_id: typing.Optional[ID] = Field(alias='resourceTypeId')
    tags: typing.Optional[TagOr]
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[Cursor]
    after: typing.Optional[Cursor]
    filter_by_resources: typing.Optional[Map] = Field(alias='filterByResources')
    payload: ResourcePoolConnection


class QueryLeafResourcePoolsQuery(Query):
    _name: str = Field('QueryLeafResourcePools', const=True)
    resource_type_id: typing.Optional[ID] = Field(alias='resourceTypeId')
    tags: typing.Optional[TagOr]
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[Cursor]
    after: typing.Optional[Cursor]
    filter_by_resources: typing.Optional[Map] = Field(alias='filterByResources')
    payload: ResourcePoolConnection


class SearchPoolsByTagsQuery(Query):
    _name: str = Field('SearchPoolsByTags', const=True)
    tags: typing.Optional[TagOr]
    first: typing.Optional[Int]
    last: typing.Optional[Int]
    before: typing.Optional[Cursor]
    after: typing.Optional[Cursor]
    payload: ResourcePoolConnection


class QueryTagsQuery(Query):
    _name: str = Field('QueryTags', const=True)


class NodeQuery(Query):
    _name: str = Field('node', const=True)
    id: ID
    payload: Node


class Resource(Payload):
    description: typing.Optional[Boolean] = Field(response='String', alias='Description', default=True)
    nested_pool: typing.Optional[ResourcePool] = Field(response='ResourcePool', alias='NestedPool')
    parent_pool: typing.Optional[ResourcePool] = Field(response='ResourcePool', alias='ParentPool')
    properties: typing.Optional[Boolean] = Field(response='Map', alias='Properties', default=True)
    alternative_id: typing.Optional[Boolean] = Field(response='Map', alias='AlternativeId', default=True)
    id: typing.Optional[Boolean] = Field(response='ID', default=True)


class ResourceConnection(Payload):
    edges: typing.Optional[ResourceEdge] = Field(response='ResourceEdge')
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(response='Int', alias='totalCount', default=True)


class ResourceEdge(Payload):
    cursor: typing.Optional[OutputCursor] = Field(response='OutputCursor')
    node: typing.Optional[Resource] = Field(response='Resource')


class ResourcePool(Payload):
    allocation_strategy: typing.Optional[AllocationStrategy] = Field(response='AllocationStrategy', alias='AllocationStrategy')
    capacity: typing.Optional[PoolCapacityPayload] = Field(response='PoolCapacityPayload', alias='Capacity')
    name: typing.Optional[Boolean] = Field(response='String', alias='Name', default=True)
    parent_resource: typing.Optional[Resource] = Field(response='Resource', alias='ParentResource')
    pool_properties: typing.Optional[Boolean] = Field(response='Map', alias='PoolProperties', default=True)
    pool_type: typing.Optional[Boolean] = Field(response='PoolType', alias='PoolType', default=True)
    resource_type: typing.Optional[ResourceType] = Field(response='ResourceType', alias='ResourceType')
    resources: typing.Optional[Resource] = Field(response='Resource', alias='Resources')
    tags: typing.Optional[Tag] = Field(response='Tag', alias='Tags')
    allocated_resources: typing.Optional[ResourceConnection] = Field(response='ResourceConnection', alias='allocatedResources')
    id: typing.Optional[Boolean] = Field(response='ID', default=True)


class ResourcePoolConnection(Payload):
    edges: typing.Optional[ResourcePoolEdge] = Field(response='ResourcePoolEdge')
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(response='Int', alias='totalCount', default=True)


class ResourcePoolEdge(Payload):
    cursor: typing.Optional[OutputCursor] = Field(response='OutputCursor')
    node: typing.Optional[ResourcePool] = Field(response='ResourcePool')


class ResourceType(Payload):
    name: typing.Optional[Boolean] = Field(response='String', alias='Name', default=True)
    pools: typing.Optional[ResourcePool] = Field(response='ResourcePool', alias='Pools')
    property_types: typing.Optional[PropertyType] = Field(response='PropertyType', alias='PropertyTypes')
    id: typing.Optional[Boolean] = Field(response='ID', default=True)


class Tag(Payload):
    pools: typing.Optional[ResourcePool] = Field(response='ResourcePool', alias='Pools')
    tag: typing.Optional[Boolean] = Field(response='String', alias='Tag', default=True)
    id: typing.Optional[Boolean] = Field(response='ID', default=True)


class TagPoolPayload(Payload):
    tag: typing.Optional[Tag] = Field(response='Tag')


class UntagPoolPayload(Payload):
    tag: typing.Optional[Tag] = Field(response='Tag')


class UpdateResourceTypeNamePayload(Payload):
    resource_type_id: typing.Optional[Boolean] = Field(response='ID', alias='resourceTypeId', default=True)


class UpdateTagPayload(Payload):
    tag: typing.Optional[Tag] = Field(response='Tag')


Node.update_forward_refs()
CreateAllocatingPoolInput.update_forward_refs()
CreateAllocationStrategyInput.update_forward_refs()
CreateNestedAllocatingPoolInput.update_forward_refs()
CreateNestedSetPoolInput.update_forward_refs()
CreateNestedSingletonPoolInput.update_forward_refs()
CreateResourceTypeInput.update_forward_refs()
CreateSetPoolInput.update_forward_refs()
CreateSingletonPoolInput.update_forward_refs()
CreateTagInput.update_forward_refs()
DeleteAllocationStrategyInput.update_forward_refs()
DeleteResourcePoolInput.update_forward_refs()
DeleteResourceTypeInput.update_forward_refs()
DeleteTagInput.update_forward_refs()
ResourceInput.update_forward_refs()
ResourcePoolInput.update_forward_refs()
TagAnd.update_forward_refs()
TagOr.update_forward_refs()
TagPoolInput.update_forward_refs()
UntagPoolInput.update_forward_refs()
UpdateResourceTypeNameInput.update_forward_refs()
UpdateTagInput.update_forward_refs()
AllocationStrategy.update_forward_refs()
CreateAllocatingPoolPayload.update_forward_refs()
CreateAllocationStrategyPayload.update_forward_refs()
CreateNestedAllocatingPoolPayload.update_forward_refs()
CreateNestedSetPoolPayload.update_forward_refs()
CreateNestedSingletonPoolPayload.update_forward_refs()
CreateResourceTypePayload.update_forward_refs()
CreateSetPoolPayload.update_forward_refs()
CreateSingletonPoolPayload.update_forward_refs()
CreateTagPayload.update_forward_refs()
DeleteAllocationStrategyPayload.update_forward_refs()
DeleteResourcePoolPayload.update_forward_refs()
DeleteResourceTypePayload.update_forward_refs()
DeleteTagPayload.update_forward_refs()
CreateTagMutation.update_forward_refs()
UpdateTagMutation.update_forward_refs()
DeleteTagMutation.update_forward_refs()
TagPoolMutation.update_forward_refs()
UntagPoolMutation.update_forward_refs()
CreateAllocationStrategyMutation.update_forward_refs()
DeleteAllocationStrategyMutation.update_forward_refs()
TestAllocationStrategyMutation.update_forward_refs()
ClaimResourceMutation.update_forward_refs()
ClaimResourceWithAltIdMutation.update_forward_refs()
FreeResourceMutation.update_forward_refs()
CreateSetPoolMutation.update_forward_refs()
CreateNestedSetPoolMutation.update_forward_refs()
CreateSingletonPoolMutation.update_forward_refs()
CreateNestedSingletonPoolMutation.update_forward_refs()
CreateAllocatingPoolMutation.update_forward_refs()
CreateNestedAllocatingPoolMutation.update_forward_refs()
DeleteResourcePoolMutation.update_forward_refs()
CreateResourceTypeMutation.update_forward_refs()
DeleteResourceTypeMutation.update_forward_refs()
UpdateResourceTypeNameMutation.update_forward_refs()
UpdateResourceAltIdMutation.update_forward_refs()
OutputCursor.update_forward_refs()
PageInfo.update_forward_refs()
PoolCapacityPayload.update_forward_refs()
PropertyType.update_forward_refs()
QueryPoolCapacityQuery.update_forward_refs()
QueryPoolTypesQuery.update_forward_refs()
QueryResourceQuery.update_forward_refs()
QueryResourcesQuery.update_forward_refs()
QueryResourcesByAltIdQuery.update_forward_refs()
QueryAllocationStrategyQuery.update_forward_refs()
QueryAllocationStrategiesQuery.update_forward_refs()
QueryResourceTypesQuery.update_forward_refs()
QueryRequiredPoolPropertiesQuery.update_forward_refs()
QueryResourcePoolQuery.update_forward_refs()
QueryEmptyResourcePoolsQuery.update_forward_refs()
QueryResourcePoolsQuery.update_forward_refs()
QueryRecentlyActiveResourcesQuery.update_forward_refs()
QueryResourcePoolHierarchyPathQuery.update_forward_refs()
QueryRootResourcePoolsQuery.update_forward_refs()
QueryLeafResourcePoolsQuery.update_forward_refs()
SearchPoolsByTagsQuery.update_forward_refs()
QueryTagsQuery.update_forward_refs()
NodeQuery.update_forward_refs()
Resource.update_forward_refs()
ResourceConnection.update_forward_refs()
ResourceEdge.update_forward_refs()
ResourcePool.update_forward_refs()
ResourcePoolConnection.update_forward_refs()
ResourcePoolEdge.update_forward_refs()
ResourceType.update_forward_refs()
Tag.update_forward_refs()
TagPoolPayload.update_forward_refs()
UntagPoolPayload.update_forward_refs()
UpdateResourceTypeNamePayload.update_forward_refs()
UpdateTagPayload.update_forward_refs()
