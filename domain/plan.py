from dataclasses import dataclass
from netboxsync.domain.common import Status
from typing import Optional

@dataclass
class EnsureSite:
    name: str
    slug: str
    status: Status

    def as_payload(self) -> dict[str, str]:
        """Return dictionary format for a payload"""
        payload = {
            'name': self.name,
            'slug': self.slug,
            'status': self.status.value # Enum to string
        }
        return payload

@dataclass
class RemoveSite:
    id: Optional[int] = None
    slug: Optional[str] = None

    def as_payload(self) -> dict[str, str]:
        """Return dictionary format for a payload"""
        if self.id is not None:
            payload = {
                'id': self.id
            }
        elif self.slug is not None:

            payload = {
                'slug': self.slug
            }
        else:
            return

        return payload