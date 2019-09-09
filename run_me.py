#!/usr/bin/env python
# Script by Mitch Bradford
# Dependencies - Netmiko, Python 3
# Instructions - List IP addresses in routers.txt and commands to run in commands.txt
# === Formatting ===
# commands.txt:
# exit
# [enable priv command]
# [enable priv command]

from netmiko import ConnectHandler
from netmiko.ssh_exception import  NetMikoTimeoutException
from paramiko.ssh_exception import SSHException 
from netmiko.ssh_exception import  AuthenticationException
from getpass import getpass
from pprint import pprint
import ipaddress

with open('commands.txt') as f:
	commands_list = f.read().splitlines()

username = input('Enter your username:')
password = getpass()

# enter IP range
ip_network_start = input('Enter the first IP: ')
ip_network_start = ipaddress.IPv4Address(ip_network_start)
ip_network_end = input('Enter the last IP: ')
ip_network_end = ipaddress.IPv4Address(ip_network_end)

def perform_tasks():
	try:
		# Actually connect to the device
		net_connect = ConnectHandler(**ios_device)  
		
		# Grab the hostname of the device, so it can be used as a filename
		hostname = net_connect.send_command("show run | i hostname")
		hostname = hostname[9:]
		
		#open file to write command output
		file = open('1 - ' + hostname + " - " + ip_address_of_device + " " + '.txt', 'w')
		# Print output to console screen
		print('-------------- Running script on ' + ip_address_of_device + ' - ' + hostname + ' ------------------')

		file.write('======== ' + ip_address_of_device + ' @ ' + hostname + ' ========')
		file.write("\n")
		
		# run and output the commands in commands.txt
		output=net_connect.send_config_set(commands_list)
		file.write(output)
		
		# Close the file	
		file.close()
		
		# Cleanly disconnect SSH session	
		#net_connect.disconnect()
	except (AuthenticationException):
		print ('Authentication Failure: ' + ip_address_of_device)
		Authfailure.write('\n' + ip_address_of_device)
	except (NetMikoTimeoutException):
		print ('\n' + 'Timeout to device: ' + ip_address_of_device)
		Timeouts.write('\n' + ip_address_of_device)
	except (SSHException):
		print ('SSH might not be enabled: ' + ip_address_of_device)
		SSHException.write('\n' + ip_address_of_device)
	except (EOFError):
		print ('\n' + 'End of attempting device: ' + ip_address_of_device)
		EOFError.write('\n' + ip_address_of_device)
	except unknown_error:
		print ('Some other error: ' + str(unknown_error))

for ip_int in range(int(ip_network_start), int(ip_network_end + 1)):
	
	ip_address_of_device = ipaddress.IPv4Address(ip_int)
	ip_address_of_device = str(ip_address_of_device)
	print ('Connecting to device ' + ip_address_of_device)
	ios_device = {
	'device_type': 'cisco_ios',
	'ip': ip_address_of_device,
	'username': username,
	'password': password
	}

	#Define the error handling files to reference if/when something fails
	Timeouts=open("Connection time outs.txt", "a")
	Authfailure=open("Auth failures.txt", "a")
	SSHException=("SSH Failure.txt", 'a')
	EOFError=("EOFerrors.txt",'a')
	UnknownError=("UnknownError.txt",'a')
	
	perform_tasks()

	