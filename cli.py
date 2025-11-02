from dotenv import load_dotenv
import os
import pynetbox

from netboxsync.domain.plan import EnsureSite
from netboxsync.domain.common import Status


# Get local env vars
load_dotenv()


nb = pynetbox.api(
    os.getenv("NETBOX_URL"),
    token=os.getenv("NETBOX_TOKEN")
)

nb.dcim.sites.create(EnsureSite(name="test", slug="test", status=Status.ACTIVE).as_payload())