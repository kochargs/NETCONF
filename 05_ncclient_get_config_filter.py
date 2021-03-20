from ncclient import manager, xml_
import always_on_devices as devices
import xml_filters as filter

with manager.connect(**devices.csr1000v, hostkey_verify=False) as m:
    res = m.get(("subtree", filter.interface))
    print(xml_.to_xml(res.data_ele, pretty_print=True))

    ## OR ##
    #
    # running_config = m.get_config("running", filter.interface)
    #
    #
    # ####
    #
    #
    # interfaces = xmltodict.parse(running_config.xml)["rpc-reply"]["data"]
    # interface = interfaces["interfaces"]["interface"]
    #
    # print(f'Interface name: { interface["name"]["#text"] }')
    # print(f'Interface description: { interface["description"] }')
    # print(f'Interface IP address: {  interface["ipv4"]["address"]["ip"] }')
    # print(f'Interface IP netmask: {  interface["ipv4"]["address"]["netmask"] }')
