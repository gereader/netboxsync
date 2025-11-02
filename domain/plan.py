from dataclasses import dataclass
from netboxsync.domain.common import Status

@dataclass
class EnsureSite:
    name: str
    slug: str
    status: Status
    delete: bool = False

    def as_payload(self) -> dict[str, str]:
        """Return dictionary format for a payload"""
        payload = {
            'name': self.name,
            'slug': self.name,
            'status': self.status.value # Enum to string
        }
        return payload