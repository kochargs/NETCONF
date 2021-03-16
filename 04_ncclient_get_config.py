from ncclient import manager
import always_on_devices as devices

with manager.connect(**devices.csr1000v, hostkey_verify=False) as m:
    m.
