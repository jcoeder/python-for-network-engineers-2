from netmiko import ConnectHandler

nxos1 = {
  'device_type': 'cisco_nxos',
  'host': 'nxos1.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
  'port': 22,
}

nxos2 = { 
  'device_type': 'cisco_nxos',
  'host': 'nxos2.lasthop.io',
  'username': 'pyclass',
  'password': '88newclass',
  'port': 22,
}

devices = [ nxos1, nxos2 ]

for device in devices:
    net_connect = ConnectHandler(**device)
    print(net_connect.send_command('show version'))
