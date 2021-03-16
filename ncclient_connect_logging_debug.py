from ncclient import manager
import logging

logging.basicConfig(level=logging.DEBUG)

device = {
        'host': 'sandbox-iosxe-latest-1.cisco.com',
        'port': '830',
        'username': 'developer',
        'password': 'C1sco12345'
        }

with manager.connect(**device, hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print(capability)
