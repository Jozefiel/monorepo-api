# generated by datamodel-codegen:
#   filename:  uniconfigV3.yaml
#   timestamp: 2023-08-03T07:32:17+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class DefaultErrorRetryPatterns:
    retry_pattern: Optional[list[str]] = None


@dataclass
class DefaultCommitErrorPatterns:
    commit_error_pattern: Optional[list[str]] = None


@dataclass
class DefaultErrorPatterns:
    error_pattern: Optional[list[str]] = None


@dataclass
class AvailableCliDeviceTranslationItem:
    default_error_retry_patterns: Optional[DefaultErrorRetryPatterns] = None
    default_commit_error_patterns: Optional[DefaultCommitErrorPatterns] = None
    device_type: Optional[str] = None
    default_error_patterns: Optional[DefaultErrorPatterns] = None
    device_version: Optional[str] = None


@dataclass
class AvailableCliDeviceTranslations:
    available_cli_device_translation: Optional[
        list[AvailableCliDeviceTranslationItem]
    ] = None