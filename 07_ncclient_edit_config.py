from ncclient import manager, xml_
import always_on_devices as devices
import xml_filters as filter
import json

with manager.connect(**devices.csr1000v, hostkey_verify=False) as m:
    res = m.edit_config(config=filter.enable_interface, target='running')
    print(xml_.to_xml(res.data_ele, pretty_print=True))
