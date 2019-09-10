# Script by Mitch Bradford
# Dependencies - Netmiko, Python 3

import ipaddress

# Enter IP range
ip_network_start = input('Enter the first IP: ')
ip_network_start = ipaddress.IPv4Address(ip_network_start)
ip_network_end = input('Enter the last IP: ')
ip_network_end = ipaddress.IPv4Address(ip_network_end)

# Create a list and populate it with the IP range
device_list = []
for ip_int in range(int(ip_network_start), int(ip_network_end + 1)):
	
	ip_address_of_device = ipaddress.IPv4Address(ip_int)
	ip_address_of_device = str(ip_address_of_device)
	device_list.append(ip_address_of_device)
