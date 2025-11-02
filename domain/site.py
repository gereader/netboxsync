from dataclasses import dataclass
from netboxsync.domain.common import Status


@dataclass
class Site:
    name: str
    slug: str
    status: Status
