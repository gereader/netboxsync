from dotenv import load_dotenv
import os
import pynetbox

from netboxsync.domain.plan import EnsureSite, RemoveSite
from netboxsync.domain.common import Status
from netboxsync.adapaters.netbox_client import NetboxClient


# Get local env vars
load_dotenv()


nb = NetboxClient(
    netbox_url=os.getenv("NETBOX_URL"),
    netbox_token=os.getenv("NETBOX_TOKEN")
)

# nb.dcim.sites.create(EnsureSite(name="test", slug="test", status=Status.ACTIVE).as_payload())
# nb.dcim.sites.delete(RemoveSite(slug="test").as_payload())
if nb.has_site(slug='test'):
    nb.delete_site(RemoveSite(slug="test"))
else:
    nb.create_site(EnsureSite(name="test", slug="test", status=Status.ACTIVE))

