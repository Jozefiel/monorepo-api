# generated by datamodel-codegen:
#   filename:  uniconfigV3.yaml

from __future__ import annotations

from enum import Enum


class AdminState(Enum):
    locked = 'locked'
    unlocked = 'unlocked'
    southbound_locked = 'southbound_locked'


class PublicKeyCipherType(Enum):
    RSA = 'RSA'
    CURVE25519 = 'CURVE25519'
    ECDSA = 'ECDSA'
