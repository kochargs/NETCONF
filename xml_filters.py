interfaces = """
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
"""

interface = """
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface>
    <name>GigabitEthernet1</name>
  </interface>
</interfaces>
"""

# send config to enable an interface.
enable_interface = """
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
      <enabled>true</enabled>
    </interface>
  </interfaces>
</config>
"""

configure_interface = """
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
      <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>2001:db8:c18:1::3</ip>
          <prefix-length>128</prefix-length>
        </address>
      </ipv6>
    </interface>
  </interfaces>
</config>
"""
