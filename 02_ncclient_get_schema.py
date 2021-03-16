from ncclient import manager
import always_on_devices as devices

device = devices.csr1000v
with manager.connect(**device, hostkey_verify=False) as m:
    print(m.get_schema('openconfig-if-ip'))
