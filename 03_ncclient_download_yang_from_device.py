from ncclient import manager
import re
import always_on_devices as devices
from rich.progress import track

device = devices.csr1000v
with manager.connect(**device, hostkey_verify=False) as m:
    for capability in track(m.server_capabilities):
        model = re.findall('module=(\S+?)(?=&|$)', capability)
        if model:
            with open(f"all_yangs\{model[0]}.yang", 'w') as f:
                f.write(str(m.get_schema(model[0])))
                
