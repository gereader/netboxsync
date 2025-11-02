from enum import StrEnum


class Status(StrEnum):
    PLANNED: str = "planned"
    STAGING: str = "staging"
    ACTIVE: str = "active"
    DECOMISSIONING: str = "decomissioning"
    RETIRED: str = "retired"