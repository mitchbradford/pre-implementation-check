from netmiko import ConnectHandler
from netmiko.ssh_exception import  NetMikoTimeoutException
from paramiko.ssh_exception import SSHException 
from netmiko.ssh_exception import  AuthenticationException
from getpass import getpass
from pprint import pprint

with open('commandsv2.txt') as f:
	commands_list = f.read().splitlines()

with open('routersv3.txt') as f:
	router_list = f.read().splitlines()

username=input('Enter your username:')
password=getpass()

for routers in router_list:
	print ('Connecting to device ' + routers)
	ip_address_of_device = routers
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
		
		output=net_connect.send_config_set(commands_list)
		print(output)
		file.write(output)
		
		# Close the file	
		file.close()
		
		# Cleanly disconnect SSH session	
		net_connect.disconnect()
	except (AuthenticationException):
		print ('Authentication Failure: ' + ip_address_of_device)
		Authfailure.write('\n' + ip_address_of_device)
		continue 
	except (NetMikoTimeoutException):
		print ('\n' + 'Timeout to device: ' + ip_address_of_device)
		Timeouts.write('\n' + ip_address_of_device)
		continue
	except (SSHException):
		print ('SSH might not be enabled: ' + ip_address_of_device)
		SSHException.write('\n' + ip_address_of_device)
		continue 
	except (EOFError):
		print ('\n' + 'End of attempting device: ' + ip_address_of_device)
		EOFError.write('\n' + ip_address_of_device)
		continue
	except unknown_error:
		print ('Some other error: ' + str(unknown_error))
		continue