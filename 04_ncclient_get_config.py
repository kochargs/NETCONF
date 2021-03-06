from ncclient import manager, xml_
import always_on_devices as devices
import xmltodict

with manager.connect(**devices.csr1000v, hostkey_verify=False) as m:
    res = m.get_config('running')
    print(xml_.to_xml(res.data_ele, pretty_print=True))
    print(xmltodict.parse(res.xml)["rpc-reply"]["data"])


