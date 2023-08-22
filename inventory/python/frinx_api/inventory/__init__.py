from __future__ import annotations

import typing

from graphql_pydantic_converter.graphql_types import ENUM
from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.graphql_types import Interface
from graphql_pydantic_converter.graphql_types import Mutation
from graphql_pydantic_converter.graphql_types import Payload
from graphql_pydantic_converter.graphql_types import Query
from graphql_pydantic_converter.graphql_types import Subscription
from pydantic import Field

ID: typing.TypeAlias = str
String: typing.TypeAlias = str
Boolean: typing.TypeAlias = bool
Int: typing.TypeAlias = int
Upload: typing.TypeAlias = typing.Any
Float: typing.TypeAlias = float


class DeviceServiceState(ENUM):
    PLANNING = 'PLANNING'
    IN_SERVICE = 'IN_SERVICE'
    OUT_OF_SERVICE = 'OUT_OF_SERVICE'


class DeviceSource(ENUM):
    MANUAL = 'MANUAL'
    DISCOVERED = 'DISCOVERED'
    IMPORTED = 'IMPORTED'


class DeviceSize(ENUM):
    SMALL = 'SMALL'
    MEDIUM = 'MEDIUM'
    LARGE = 'LARGE'


class SortDeviceBy(ENUM):
    NAME = 'NAME'
    CREATED_AT = 'CREATED_AT'


class SortDirection(ENUM):
    ASC = 'ASC'
    DESC = 'DESC'


class GraphEdgeStatus(ENUM):
    ok = 'ok'
    unknown = 'unknown'


class Node(Interface):
    id: typing.Optional[Boolean]


class BaseGraphNode(Interface):
    id: typing.Optional[Boolean]
    interfaces: typing.Optional[GraphNodeInterface]
    coordinates: typing.Optional[GraphNodeCoordinates]
    device_type: typing.Optional[Boolean] = Field(alias='deviceType')
    software_version: typing.Optional[Boolean] = Field(alias='softwareVersion')


class FilterDevicesInput(Input):
    labels: typing.Optional[list[String]]
    device_name: typing.Optional[String] = Field(alias='deviceName')


class DeviceOrderByInput(Input):
    sort_key: SortDeviceBy = Field(alias='sortKey')
    direction: SortDirection


class AddDeviceInput(Input):
    name: String
    zone_id: String = Field(alias='zoneId')
    label_ids: typing.Optional[list[String]] = Field(alias='labelIds')
    device_size: typing.Optional[DeviceSize] = Field(alias='deviceSize')
    service_state: typing.Optional[DeviceServiceState] = Field(alias='serviceState')
    mount_parameters: typing.Optional[String] = Field(alias='mountParameters')
    blueprint_id: typing.Optional[String] = Field(alias='blueprintId')
    model: typing.Optional[String]
    vendor: typing.Optional[String]
    address: typing.Optional[String]
    username: typing.Optional[String]
    password: typing.Optional[String]
    port: typing.Optional[Int]
    device_type: typing.Optional[String] = Field(alias='deviceType')
    version: typing.Optional[String]


class UpdateDeviceInput(Input):
    mount_parameters: typing.Optional[String] = Field(alias='mountParameters')
    blueprint_id: typing.Optional[String] = Field(alias='blueprintId')
    model: typing.Optional[String]
    vendor: typing.Optional[String]
    address: typing.Optional[String]
    username: typing.Optional[String]
    password: typing.Optional[String]
    port: typing.Optional[Int]
    device_type: typing.Optional[String] = Field(alias='deviceType')
    device_size: typing.Optional[DeviceSize] = Field(alias='deviceSize')
    version: typing.Optional[String]
    label_ids: typing.Optional[list[String]] = Field(alias='labelIds')
    service_state: typing.Optional[DeviceServiceState] = Field(alias='serviceState')
    location_id: typing.Optional[String] = Field(alias='locationId')


class CSVImportInput(Input):
    zone_id: String = Field(alias='zoneId')
    file: Upload


class AddZoneInput(Input):
    name: String


class UpdateDataStoreInput(Input):
    config: String


class CommitConfigInput(Input):
    device_id: String = Field(alias='deviceId')
    should_dry_run: typing.Optional[Boolean] = Field(alias='shouldDryRun')


class AddSnapshotInput(Input):
    name: String
    device_id: String = Field(alias='deviceId')


class DeleteSnapshotInput(Input):
    device_id: String = Field(alias='deviceId')
    name: String
    transaction_id: String = Field(alias='transactionId')


class ApplySnapshotInput(Input):
    device_id: String = Field(alias='deviceId')
    name: String


class AddLocationInput(Input):
    name: String
    country_id: String = Field(alias='countryId')


class AddBlueprintInput(Input):
    name: String
    template: String


class UpdateBlueprintInput(Input):
    name: typing.Optional[String]
    template: typing.Optional[String]


class FilterTopologyInput(Input):
    labels: typing.Optional[list[String]]


class GraphNodeCoordinatesInput(Input):
    device_name: String = Field(alias='deviceName')
    x: Float
    y: Float


class CreateLabelInput(Input):
    name: String


class PageInfo(Payload):
    start_cursor: typing.Optional[Boolean] = Field(response='String', alias='startCursor', default=True)
    end_cursor: typing.Optional[Boolean] = Field(response='String', alias='endCursor', default=True)
    has_next_page: typing.Optional[Boolean] = Field(response='Boolean', alias='hasNextPage', default=True)
    has_previous_page: typing.Optional[Boolean] = Field(response='Boolean', alias='hasPreviousPage', default=True)


class Device(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    created_at: typing.Optional[Boolean] = Field(response='String', alias='createdAt', default=True)
    updated_at: typing.Optional[Boolean] = Field(response='String', alias='updatedAt', default=True)
    model: typing.Optional[Boolean] = Field(response='String', default=True)
    vendor: typing.Optional[Boolean] = Field(response='String', default=True)
    port: typing.Optional[Boolean] = Field(response='Int', default=True)
    address: typing.Optional[Boolean] = Field(response='String', default=True)
    mount_parameters: typing.Optional[Boolean] = Field(response='String', alias='mountParameters', default=True)
    source: typing.Optional[Boolean] = Field(response='DeviceSource', default=True)
    service_state: typing.Optional[Boolean] = Field(response='DeviceServiceState', alias='serviceState', default=True)
    is_installed: typing.Optional[Boolean] = Field(response='Boolean', alias='isInstalled', default=True)
    zone: typing.Optional[Zone] = Field(response='Zone')
    labels: typing.Optional[LabelConnection] = Field(response='LabelConnection')
    location: typing.Optional[Location] = Field(response='Location')
    device_size: typing.Optional[Boolean] = Field(response='DeviceSize', alias='deviceSize', default=True)
    blueprint: typing.Optional[Blueprint] = Field(response='Blueprint')


class DeviceEdge(Payload):
    node: typing.Optional[Device] = Field(response='Device')
    cursor: typing.Optional[Boolean] = Field(response='String', default=True)


class DeviceConnection(Payload):
    edges: typing.Optional[DeviceEdge] = Field(response='DeviceEdge')
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(response='Int', alias='totalCount', default=True)


class AddDevicePayload(Payload):
    device: typing.Optional[Device] = Field(response='Device')


class UpdateDevicePayload(Payload):
    device: typing.Optional[Device] = Field(response='Device')


class UpdateDeviceMetadataPayload(Payload):
    devices: typing.Optional[Device] = Field(response='Device')


class DeleteDevicePayload(Payload):
    device: typing.Optional[Device] = Field(response='Device')


class InstallDevicePayload(Payload):
    device: typing.Optional[Device] = Field(response='Device')


class UninstallDevicePayload(Payload):
    device: typing.Optional[Device] = Field(response='Device')


class CSVImport(Payload):
    is_ok: typing.Optional[Boolean] = Field(response='Boolean', alias='isOk', default=True)


class Zone(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    created_at: typing.Optional[Boolean] = Field(response='String', alias='createdAt', default=True)
    updated_at: typing.Optional[Boolean] = Field(response='String', alias='updatedAt', default=True)


class ZoneEdge(Payload):
    node: typing.Optional[Zone] = Field(response='Zone')
    cursor: typing.Optional[Boolean] = Field(response='String', default=True)


class ZonesConnection(Payload):
    edges: typing.Optional[ZoneEdge] = Field(response='ZoneEdge')
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(response='Int', alias='totalCount', default=True)


class AddZonePayload(Payload):
    zone: typing.Optional[Zone] = Field(response='Zone')


class Snapshot(Payload):
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    created_at: typing.Optional[Boolean] = Field(response='String', alias='createdAt', default=True)


class DataStore(Payload):
    config: typing.Optional[Boolean] = Field(response='String', default=True)
    operational: typing.Optional[Boolean] = Field(response='String', default=True)
    snapshots: typing.Optional[Snapshot] = Field(response='Snapshot')


class UpdateDataStorePayload(Payload):
    data_store: typing.Optional[DataStore] = Field(response='DataStore', alias='dataStore')


class CommitConfigOutput(Payload):
    device_id: typing.Optional[Boolean] = Field(response='String', alias='deviceId', default=True)
    message: typing.Optional[Boolean] = Field(response='String', default=True)
    configuration: typing.Optional[Boolean] = Field(response='String', default=True)


class CommitConfigPayload(Payload):
    output: typing.Optional[CommitConfigOutput] = Field(response='CommitConfigOutput')


class ResetConfigPayload(Payload):
    data_store: typing.Optional[DataStore] = Field(response='DataStore', alias='dataStore')


class AddSnapshotPayload(Payload):
    snapshot: typing.Optional[Snapshot] = Field(response='Snapshot')


class DeleteSnapshotPayload(Payload):
    snapshot: typing.Optional[Snapshot] = Field(response='Snapshot')


class ApplySnapshotPayload(Payload):
    is_ok: typing.Optional[Boolean] = Field(response='Boolean', alias='isOk', default=True)
    output: typing.Optional[Boolean] = Field(response='String', default=True)


class DiffData(Payload):
    path: typing.Optional[Boolean] = Field(response='String', default=True)
    data: typing.Optional[Boolean] = Field(response='String', default=True)


class CalculatedUpdateDiffData(Payload):
    path: typing.Optional[Boolean] = Field(response='String', default=True)
    intended_data: typing.Optional[Boolean] = Field(response='String', alias='intendedData', default=True)
    actual_data: typing.Optional[Boolean] = Field(response='String', alias='actualData', default=True)


class CalculatedDiffResult(Payload):
    created_data: typing.Optional[DiffData] = Field(response='DiffData', alias='createdData')
    deleted_data: typing.Optional[DiffData] = Field(response='DiffData', alias='deletedData')
    updated_data: typing.Optional[CalculatedUpdateDiffData] = Field(response='CalculatedUpdateDiffData', alias='updatedData')


class CalculatedDiffPayload(Payload):
    result: typing.Optional[CalculatedDiffResult] = Field(response='CalculatedDiffResult')


class SyncFromNetworkPayload(Payload):
    data_store: typing.Optional[DataStore] = Field(response='DataStore', alias='dataStore')


class Label(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    created_at: typing.Optional[Boolean] = Field(response='String', alias='createdAt', default=True)
    updated_at: typing.Optional[Boolean] = Field(response='String', alias='updatedAt', default=True)


class LabelEdge(Payload):
    node: typing.Optional[Label] = Field(response='Label')
    cursor: typing.Optional[Boolean] = Field(response='String', default=True)


class LabelConnection(Payload):
    edges: typing.Optional[LabelEdge] = Field(response='LabelEdge')
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(response='Int', alias='totalCount', default=True)


class CreateLabelPayload(Payload):
    label: typing.Optional[Label] = Field(response='Label')


class DeleteLabelPayload(Payload):
    label: typing.Optional[Label] = Field(response='Label')


class Location(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    created_at: typing.Optional[Boolean] = Field(response='String', alias='createdAt', default=True)
    updated_at: typing.Optional[Boolean] = Field(response='String', alias='updatedAt', default=True)
    country: typing.Optional[Boolean] = Field(response='String', default=True)


class Country(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    code: typing.Optional[Boolean] = Field(response='String', default=True)


class CountryEdge(Payload):
    node: typing.Optional[Country] = Field(response='Country')
    cursor: typing.Optional[Boolean] = Field(response='String', default=True)


class CountryConnection(Payload):
    edges: typing.Optional[CountryEdge] = Field(response='CountryEdge')
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(response='Int', alias='totalCount', default=True)


class LocationEdge(Payload):
    node: typing.Optional[Location] = Field(response='Location')
    cursor: typing.Optional[Boolean] = Field(response='String', default=True)


class LocationConnection(Payload):
    edges: typing.Optional[LocationEdge] = Field(response='LocationEdge')
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(response='Int', alias='totalCount', default=True)


class AddLocationPayload(Payload):
    location: typing.Optional[Location] = Field(response='Location')


class Blueprint(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    created_at: typing.Optional[Boolean] = Field(response='String', alias='createdAt', default=True)
    updated_at: typing.Optional[Boolean] = Field(response='String', alias='updatedAt', default=True)
    template: typing.Optional[Boolean] = Field(response='String', default=True)


class BlueprintEdge(Payload):
    node: typing.Optional[Blueprint] = Field(response='Blueprint')
    cursor: typing.Optional[Boolean] = Field(response='String', default=True)


class BlueprintConnection(Payload):
    edges: typing.Optional[BlueprintEdge] = Field(response='BlueprintEdge')
    page_info: typing.Optional[PageInfo] = Field(response='PageInfo', alias='pageInfo')
    total_count: typing.Optional[Boolean] = Field(response='Int', alias='totalCount', default=True)


class AddBlueprintPayload(Payload):
    blueprint: typing.Optional[Blueprint] = Field(response='Blueprint')


class UpdateBlueprintPayload(Payload):
    blueprint: typing.Optional[Blueprint] = Field(response='Blueprint')


class DeleteBlueprintPayload(Payload):
    blueprint: typing.Optional[Blueprint] = Field(response='Blueprint')


class TransactionDiff(Payload):
    path: typing.Optional[Boolean] = Field(response='String', default=True)
    data_before: typing.Optional[Boolean] = Field(response='String', alias='dataBefore', default=True)
    data_after: typing.Optional[Boolean] = Field(response='String', alias='dataAfter', default=True)


class TransactionChange(Payload):
    device: typing.Optional[Device] = Field(response='Device')
    diff: typing.Optional[TransactionDiff] = Field(response='TransactionDiff')


class Transaction(Payload):
    transaction_id: typing.Optional[Boolean] = Field(response='String', alias='transactionId', default=True)
    last_commit_time: typing.Optional[Boolean] = Field(response='String', alias='lastCommitTime', default=True)
    changes: typing.Optional[TransactionChange] = Field(response='TransactionChange')


class CreateTransactionPayload(Payload):
    transaction_id: typing.Optional[Boolean] = Field(response='String', alias='transactionId', default=True)


class CloseTransactionPayload(Payload):
    is_ok: typing.Optional[Boolean] = Field(response='Boolean', alias='isOk', default=True)


class RevertChangesPayload(Payload):
    is_ok: typing.Optional[Boolean] = Field(response='Boolean', alias='isOk', default=True)


class GraphNodeInterface(Payload):
    id: typing.Optional[Boolean] = Field(response='String', default=True)
    status: typing.Optional[Boolean] = Field(response='GraphEdgeStatus', default=True)
    name: typing.Optional[Boolean] = Field(response='String', default=True)


class GraphNodeCoordinates(Payload):
    x: typing.Optional[Boolean] = Field(response='Float', default=True)
    y: typing.Optional[Boolean] = Field(response='Float', default=True)


class GraphNode(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    interfaces: typing.Optional[GraphNodeInterface] = Field(response='GraphNodeInterface')
    coordinates: typing.Optional[GraphNodeCoordinates] = Field(response='GraphNodeCoordinates')
    device_type: typing.Optional[Boolean] = Field(response='String', alias='deviceType', default=True)
    software_version: typing.Optional[Boolean] = Field(response='String', alias='softwareVersion', default=True)
    device: typing.Optional[Device] = Field(response='Device')


class EdgeSourceTarget(Payload):
    node_id: typing.Optional[Boolean] = Field(response='String', alias='nodeId', default=True)
    interface: typing.Optional[Boolean] = Field(response='String', default=True)


class GraphEdge(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    source: typing.Optional[EdgeSourceTarget] = Field(response='EdgeSourceTarget')
    target: typing.Optional[EdgeSourceTarget] = Field(response='EdgeSourceTarget')


class Topology(Payload):
    nodes: typing.Optional[GraphNode] = Field(response='GraphNode')
    edges: typing.Optional[GraphEdge] = Field(response='GraphEdge')


class GraphVersionEdge(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    source: typing.Optional[EdgeSourceTarget] = Field(response='EdgeSourceTarget')
    target: typing.Optional[EdgeSourceTarget] = Field(response='EdgeSourceTarget')


class TopologyVersionData(Payload):
    nodes: typing.Optional[GraphVersionNode] = Field(response='GraphVersionNode')
    edges: typing.Optional[GraphVersionEdge] = Field(response='GraphVersionEdge')


class TopologyCommonNodes(Payload):
    common_nodes: typing.Optional[Boolean] = Field(response='String', alias='commonNodes', default=True)


class UpdateGraphNodeCoordinatesPayload(Payload):
    device_names: typing.Optional[Boolean] = Field(response='String', alias='deviceNames', default=True)


class NetInterface(Payload):
    id: typing.Optional[Boolean] = Field(response='String', default=True)
    name: typing.Optional[Boolean] = Field(response='String', default=True)


class NetNetwork(Payload):
    id: typing.Optional[Boolean] = Field(response='String', default=True)
    subnet: typing.Optional[Boolean] = Field(response='String', default=True)
    coordinates: typing.Optional[GraphNodeCoordinates] = Field(response='GraphNodeCoordinates')


class NetNode(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    name: typing.Optional[Boolean] = Field(response='String', default=True)
    interfaces: typing.Optional[NetInterface] = Field(response='NetInterface')
    networks: typing.Optional[NetNetwork] = Field(response='NetNetwork')
    coordinates: typing.Optional[GraphNodeCoordinates] = Field(response='GraphNodeCoordinates')


class NetTopology(Payload):
    edges: typing.Optional[GraphEdge] = Field(response='GraphEdge')
    nodes: typing.Optional[NetNode] = Field(response='NetNode')


class GraphVersionNode(Payload):
    id: typing.Optional[Boolean] = Field(response='ID', default=True)
    interfaces: typing.Optional[GraphNodeInterface] = Field(response='GraphNodeInterface')
    coordinates: typing.Optional[GraphNodeCoordinates] = Field(response='GraphNodeCoordinates')
    device_type: typing.Optional[Boolean] = Field(response='String', alias='deviceType', default=True)
    software_version: typing.Optional[Boolean] = Field(response='String', alias='softwareVersion', default=True)
    name: typing.Optional[Boolean] = Field(response='String', default=True)


class NodeQuery(Query):
    _name: str = Field('node', const=True)
    id: ID
    payload: Node


class DevicesQuery(Query):
    _name: str = Field('devices', const=True)
    first: typing.Optional[Int]
    after: typing.Optional[String]
    last: typing.Optional[Int]
    before: typing.Optional[String]
    filter: typing.Optional[FilterDevicesInput]
    order_by: typing.Optional[DeviceOrderByInput] = Field(alias='orderBy')
    payload: DeviceConnection


class UniconfigShellSessionQuery(Query):
    _name: str = Field('uniconfigShellSession', const=True)


class ZonesQuery(Query):
    _name: str = Field('zones', const=True)
    first: typing.Optional[Int]
    after: typing.Optional[String]
    last: typing.Optional[Int]
    before: typing.Optional[String]
    payload: ZonesConnection


class DataStoreQuery(Query):
    _name: str = Field('dataStore', const=True)
    device_id: String = Field(alias='deviceId')
    transaction_id: String = Field(alias='transactionId')
    payload: DataStore


class CalculatedDiffQuery(Query):
    _name: str = Field('calculatedDiff', const=True)
    device_id: String = Field(alias='deviceId')
    transaction_id: String = Field(alias='transactionId')
    payload: CalculatedDiffPayload


class LabelsQuery(Query):
    _name: str = Field('labels', const=True)
    first: typing.Optional[Int]
    after: typing.Optional[String]
    last: typing.Optional[Int]
    before: typing.Optional[String]
    payload: LabelConnection


class CountriesQuery(Query):
    _name: str = Field('countries', const=True)
    first: typing.Optional[Int]
    after: typing.Optional[String]
    last: typing.Optional[Int]
    before: typing.Optional[String]
    payload: CountryConnection


class LocationsQuery(Query):
    _name: str = Field('locations', const=True)
    first: typing.Optional[Int]
    after: typing.Optional[String]
    last: typing.Optional[Int]
    before: typing.Optional[String]
    payload: LocationConnection


class BlueprintsQuery(Query):
    _name: str = Field('blueprints', const=True)
    first: typing.Optional[Int]
    after: typing.Optional[String]
    last: typing.Optional[Int]
    before: typing.Optional[String]
    payload: BlueprintConnection


class TransactionsQuery(Query):
    _name: str = Field('transactions', const=True)


class TopologyQuery(Query):
    _name: str = Field('topology', const=True)
    filter: typing.Optional[FilterTopologyInput]
    payload: Topology


class TopologyVersionsQuery(Query):
    _name: str = Field('topologyVersions', const=True)


class TopologyCommonNodesQuery(Query):
    _name: str = Field('topologyCommonNodes', const=True)
    nodes: typing.Optional[list[String]]
    payload: TopologyCommonNodes


class TopologyVersionDataQuery(Query):
    _name: str = Field('topologyVersionData', const=True)
    version: String
    payload: TopologyVersionData


class NetTopologyQuery(Query):
    _name: str = Field('netTopology', const=True)


class AddDeviceMutation(Mutation):
    _name: str = Field('addDevice', const=True)
    input: AddDeviceInput
    payload: AddDevicePayload


class UpdateDeviceMutation(Mutation):
    _name: str = Field('updateDevice', const=True)
    id: String
    input: UpdateDeviceInput
    payload: UpdateDevicePayload


class DeleteDeviceMutation(Mutation):
    _name: str = Field('deleteDevice', const=True)
    id: String
    payload: DeleteDevicePayload


class InstallDeviceMutation(Mutation):
    _name: str = Field('installDevice', const=True)
    id: String
    payload: InstallDevicePayload


class UninstallDeviceMutation(Mutation):
    _name: str = Field('uninstallDevice', const=True)
    id: String
    payload: UninstallDevicePayload


class ImportCSVMutation(Mutation):
    _name: str = Field('importCSV', const=True)
    input: CSVImportInput
    payload: CSVImport


class AddZoneMutation(Mutation):
    _name: str = Field('addZone', const=True)
    input: AddZoneInput
    payload: AddZonePayload


class UpdateDataStoreMutation(Mutation):
    _name: str = Field('updateDataStore', const=True)
    device_id: String = Field(alias='deviceId')
    transaction_id: String = Field(alias='transactionId')
    input: UpdateDataStoreInput
    payload: UpdateDataStorePayload


class CommitConfigMutation(Mutation):
    _name: str = Field('commitConfig', const=True)
    transaction_id: String = Field(alias='transactionId')
    input: CommitConfigInput
    payload: CommitConfigPayload


class ResetConfigMutation(Mutation):
    _name: str = Field('resetConfig', const=True)
    device_id: String = Field(alias='deviceId')
    transaction_id: String = Field(alias='transactionId')
    payload: ResetConfigPayload


class AddSnapshotMutation(Mutation):
    _name: str = Field('addSnapshot', const=True)
    input: AddSnapshotInput
    transaction_id: String = Field(alias='transactionId')
    payload: AddSnapshotPayload


class DeleteSnapshotMutation(Mutation):
    _name: str = Field('deleteSnapshot', const=True)
    input: DeleteSnapshotInput
    payload: DeleteSnapshotPayload


class ApplySnapshotMutation(Mutation):
    _name: str = Field('applySnapshot', const=True)
    input: ApplySnapshotInput
    transaction_id: String = Field(alias='transactionId')
    payload: ApplySnapshotPayload


class SyncFromNetworkMutation(Mutation):
    _name: str = Field('syncFromNetwork', const=True)
    device_id: String = Field(alias='deviceId')
    transaction_id: String = Field(alias='transactionId')
    payload: SyncFromNetworkPayload


class CreateLabelMutation(Mutation):
    _name: str = Field('createLabel', const=True)
    input: CreateLabelInput
    payload: CreateLabelPayload


class DeleteLabelMutation(Mutation):
    _name: str = Field('deleteLabel', const=True)
    id: String
    payload: DeleteLabelPayload


class AddLocationMutation(Mutation):
    _name: str = Field('addLocation', const=True)
    input: AddLocationInput
    payload: AddLocationPayload


class AddBlueprintMutation(Mutation):
    _name: str = Field('addBlueprint', const=True)
    input: AddBlueprintInput
    payload: AddBlueprintPayload


class UpdateBlueprintMutation(Mutation):
    _name: str = Field('updateBlueprint', const=True)
    id: String
    input: UpdateBlueprintInput
    payload: UpdateBlueprintPayload


class DeleteBlueprintMutation(Mutation):
    _name: str = Field('deleteBlueprint', const=True)
    id: String
    payload: DeleteBlueprintPayload


class CreateTransactionMutation(Mutation):
    _name: str = Field('createTransaction', const=True)
    device_id: String = Field(alias='deviceId')
    payload: CreateTransactionPayload


class CloseTransactionMutation(Mutation):
    _name: str = Field('closeTransaction', const=True)
    device_id: String = Field(alias='deviceId')
    transaction_id: String = Field(alias='transactionId')
    payload: CloseTransactionPayload


class RevertChangesMutation(Mutation):
    _name: str = Field('revertChanges', const=True)
    transaction_id: String = Field(alias='transactionId')
    payload: RevertChangesPayload


class UpdateGraphNodeCoordinatesMutation(Mutation):
    _name: str = Field('updateGraphNodeCoordinates', const=True)
    input: typing.Optional[list[GraphNodeCoordinatesInput]]
    payload: UpdateGraphNodeCoordinatesPayload


class UniconfigShellSubscription(Subscription):
    _name: str = Field('uniconfigShell', const=True)
    input: typing.Optional[String]
    trigger: typing.Optional[Int]
    session_id: String = Field(alias='sessionId')
    payload: Boolean


Node.update_forward_refs()
BaseGraphNode.update_forward_refs()
FilterDevicesInput.update_forward_refs()
DeviceOrderByInput.update_forward_refs()
AddDeviceInput.update_forward_refs()
UpdateDeviceInput.update_forward_refs()
CSVImportInput.update_forward_refs()
AddZoneInput.update_forward_refs()
UpdateDataStoreInput.update_forward_refs()
CommitConfigInput.update_forward_refs()
AddSnapshotInput.update_forward_refs()
DeleteSnapshotInput.update_forward_refs()
ApplySnapshotInput.update_forward_refs()
AddLocationInput.update_forward_refs()
AddBlueprintInput.update_forward_refs()
UpdateBlueprintInput.update_forward_refs()
FilterTopologyInput.update_forward_refs()
GraphNodeCoordinatesInput.update_forward_refs()
CreateLabelInput.update_forward_refs()
PageInfo.update_forward_refs()
Device.update_forward_refs()
DeviceEdge.update_forward_refs()
DeviceConnection.update_forward_refs()
AddDevicePayload.update_forward_refs()
UpdateDevicePayload.update_forward_refs()
UpdateDeviceMetadataPayload.update_forward_refs()
DeleteDevicePayload.update_forward_refs()
InstallDevicePayload.update_forward_refs()
UninstallDevicePayload.update_forward_refs()
CSVImport.update_forward_refs()
Zone.update_forward_refs()
ZoneEdge.update_forward_refs()
ZonesConnection.update_forward_refs()
AddZonePayload.update_forward_refs()
Snapshot.update_forward_refs()
DataStore.update_forward_refs()
UpdateDataStorePayload.update_forward_refs()
CommitConfigOutput.update_forward_refs()
CommitConfigPayload.update_forward_refs()
ResetConfigPayload.update_forward_refs()
AddSnapshotPayload.update_forward_refs()
DeleteSnapshotPayload.update_forward_refs()
ApplySnapshotPayload.update_forward_refs()
DiffData.update_forward_refs()
CalculatedUpdateDiffData.update_forward_refs()
CalculatedDiffResult.update_forward_refs()
CalculatedDiffPayload.update_forward_refs()
SyncFromNetworkPayload.update_forward_refs()
Label.update_forward_refs()
LabelEdge.update_forward_refs()
LabelConnection.update_forward_refs()
CreateLabelPayload.update_forward_refs()
DeleteLabelPayload.update_forward_refs()
Location.update_forward_refs()
Country.update_forward_refs()
CountryEdge.update_forward_refs()
CountryConnection.update_forward_refs()
LocationEdge.update_forward_refs()
LocationConnection.update_forward_refs()
AddLocationPayload.update_forward_refs()
Blueprint.update_forward_refs()
BlueprintEdge.update_forward_refs()
BlueprintConnection.update_forward_refs()
AddBlueprintPayload.update_forward_refs()
UpdateBlueprintPayload.update_forward_refs()
DeleteBlueprintPayload.update_forward_refs()
TransactionDiff.update_forward_refs()
TransactionChange.update_forward_refs()
Transaction.update_forward_refs()
CreateTransactionPayload.update_forward_refs()
CloseTransactionPayload.update_forward_refs()
RevertChangesPayload.update_forward_refs()
GraphNodeInterface.update_forward_refs()
GraphNodeCoordinates.update_forward_refs()
GraphNode.update_forward_refs()
EdgeSourceTarget.update_forward_refs()
GraphEdge.update_forward_refs()
Topology.update_forward_refs()
GraphVersionEdge.update_forward_refs()
TopologyVersionData.update_forward_refs()
TopologyCommonNodes.update_forward_refs()
UpdateGraphNodeCoordinatesPayload.update_forward_refs()
NetInterface.update_forward_refs()
NetNetwork.update_forward_refs()
NetNode.update_forward_refs()
NetTopology.update_forward_refs()
GraphVersionNode.update_forward_refs()
NodeQuery.update_forward_refs()
DevicesQuery.update_forward_refs()
UniconfigShellSessionQuery.update_forward_refs()
ZonesQuery.update_forward_refs()
DataStoreQuery.update_forward_refs()
CalculatedDiffQuery.update_forward_refs()
LabelsQuery.update_forward_refs()
CountriesQuery.update_forward_refs()
LocationsQuery.update_forward_refs()
BlueprintsQuery.update_forward_refs()
TransactionsQuery.update_forward_refs()
TopologyQuery.update_forward_refs()
TopologyVersionsQuery.update_forward_refs()
TopologyCommonNodesQuery.update_forward_refs()
TopologyVersionDataQuery.update_forward_refs()
NetTopologyQuery.update_forward_refs()
AddDeviceMutation.update_forward_refs()
UpdateDeviceMutation.update_forward_refs()
DeleteDeviceMutation.update_forward_refs()
InstallDeviceMutation.update_forward_refs()
UninstallDeviceMutation.update_forward_refs()
ImportCSVMutation.update_forward_refs()
AddZoneMutation.update_forward_refs()
UpdateDataStoreMutation.update_forward_refs()
CommitConfigMutation.update_forward_refs()
ResetConfigMutation.update_forward_refs()
AddSnapshotMutation.update_forward_refs()
DeleteSnapshotMutation.update_forward_refs()
ApplySnapshotMutation.update_forward_refs()
SyncFromNetworkMutation.update_forward_refs()
CreateLabelMutation.update_forward_refs()
DeleteLabelMutation.update_forward_refs()
AddLocationMutation.update_forward_refs()
AddBlueprintMutation.update_forward_refs()
UpdateBlueprintMutation.update_forward_refs()
DeleteBlueprintMutation.update_forward_refs()
CreateTransactionMutation.update_forward_refs()
CloseTransactionMutation.update_forward_refs()
RevertChangesMutation.update_forward_refs()
UpdateGraphNodeCoordinatesMutation.update_forward_refs()
UniconfigShellSubscription.update_forward_refs()
