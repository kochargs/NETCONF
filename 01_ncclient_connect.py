from ncclient import manager
import always_on_devices as devices

device = devices.csr1000v
with manager.connect(**device, hostkey_verify=False) as m:
    print(m.connected)
    if m.connected():
        for capability in m.server_capabilities:
            print(capability)
    else:
        print("Device connection not successful")
