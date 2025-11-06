import pynetbox
from netboxsync.domain.plan import EnsureSite, RemoveSite
from typing import Optional

class NetboxClient:
    def __init__(self, netbox_url: str, netbox_token: str, threading: bool = False, strict_filters: bool = False):
        self.netbox_url = netbox_url
        self.netbox_token = netbox_token
        self.threading = threading
        self.strict_filters = strict_filters
        self._nb = pynetbox.api(
            url = self.netbox_url,
            token = self.netbox_token,
            threading = self.threading,
        )

    def has_site(self, slug: Optional[str] = None, id: Optional[int] = None) -> bool:
        if id is not None:
            nb_site = self._nb.dcim.sites.get(id=id)            
        elif slug is not None:
            nb_site = self._nb.dcim.sites.get(slug=slug)
        else:
            raise ValueError("You must provide a valid id or slug to to determine if site exists.")
        
        # Better than if/else return logic because either it exists or it doesn't
        return bool(nb_site)

    def create_site(self, site: EnsureSite) -> None:
        self._nb.dcim.sites.create(site.as_payload())

    def delete_site(self, site: RemoveSite) -> None:
        if site.id is not None:
            nb_site = self._nb.dcim.sites.get(id=site.id)
            if nb_site:
                nb_site.delete()
        elif site.slug is not None:
            nb_site = self._nb.dcim.sites.get(slug=site.slug)
            if nb_site:
                nb_site.delete()
        else:
            raise ValueError("You must provide a valid id or slug to delete.")

