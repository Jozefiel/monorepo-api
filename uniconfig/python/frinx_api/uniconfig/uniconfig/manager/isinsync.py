# generated by datamodel-codegen:
#   filename:  uniconfigV3.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from ...frinx import types


class TargetNodes(BaseModel):
    class Config:
        allow_population_by_field_name = True

    node: Optional[list[str]] = None


class Input(BaseModel):
    class Config:
        allow_population_by_field_name = True

    target_nodes: Optional[TargetNodes] = Field(
        None,
        alias='target-nodes',
        title='uniconfig.manager.targetuniconfignodesfields.TargetNodes',
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
    is_in_sync: Optional[bool] = Field(None, alias='is-in-sync')
    status: types.OperationResultType


class NodeResults(BaseModel):
    class Config:
        allow_population_by_field_name = True

    node_result: Optional[list[NodeResultItem]] = Field(None, alias='node-result')
    """
    Result of is-in-sync operation on the given node.
    """


class Output(BaseModel):
    class Config:
        allow_population_by_field_name = True

    error_message: Optional[str] = Field(None, alias='error-message')
    """
    Error message that describe overall problem.
    """
    node_results: Optional[NodeResults] = Field(
        None,
        alias='node-results',
        title='uniconfig.manager.isinsyncoutputfields.NodeResults',
    )
    """
    Result of checking if network elements are in-sync with operational datastore.
    """
    overall_status: types.OperationResultType = Field(..., alias='overall-status')