#!/usr/bin/env python
# Script by Mitch Bradford
# Dependencies - Netmiko, Python 3
# Instructions - List commands to run in commands.txt
# === Formatting ===
# commands.txt:
# exit
# [enable priv command]
# [enable priv command]

# -----------------------------------------------------------------------
import threading
from datetime import datetime
#from datetime import timezone
from netmiko import ConnectHandler
from my_devices import device_list as devices
from netmiko.ssh_exception import  NetMikoTimeoutException
from paramiko.ssh_exception import SSHException 
from netmiko.ssh_exception import  AuthenticationException
from getpass import getpass
from pprint import pprint

# -----------------------------------------------------------------------
# Define the error handling files to reference if/when something fails
Timeouts=open("Connection timeouts.txt", "a")
Authfailure=open("Auth failures.txt", "a")
SSHException=("SSH failures.txt", 'a')
EOFError=("EOF errors.txt",'a')
UnknownError=("Unknown errors.txt",'a')

with open('commands.txt') as f:
	commands_list = f.read().splitlines()

username = input('Enter your username:')
password = getpass("Enter your password: ")

# -----------------------------------------------------------------------
def run_commands(a_device):
	"""
	Function using Netmiko to connect to each of the devices. Execute
	commands on each device from commands.txt
	"""
	
	# Network device definition for Netmiko
	ios_device = {
	'device_type': 'cisco_ios',
	'ip': a_device,
	'username': username,
	'password': password,
	}
	
	# Connect to device, run commands, output to file
	try:
		current_time = datetime.now().strftime("%y_%m_%d_%H%M")

		print ('Connecting to device ' + a_device)
		remote_conn = ConnectHandler(**ios_device)
		
		# Grab the hostname of the device, so it can be used as a filename
		hostname = remote_conn.send_command("show run | i hostname")
		hostname = hostname[9:]
		
		#open file to write command output
		file = open(hostname + " - " + a_device + " " + current_time + '.txt', 'w')
		# Print output to console screen
		print('-------------- Running script on ' + a_device + ' - ' + hostname + ' ------------------')
		
		file.write('======== ' + a_device + ' @ ' + hostname + ' ========')
		file.write("\n")
		
		# run and output the commands in commands.txt
		output=remote_conn.send_config_set(commands_list)
		file.write(output)
		
		# Close the file	
		file.close()
		
		# Cleanly disconnect SSH session	
		remote_conn.disconnect()
		
	except (AuthenticationException):
		print ('Authentication Failure: ' + a_device)
		Authfailure.write('\n' + a_device)
	except (NetMikoTimeoutException):
		print ('\n' + 'Timeout to device: ' + a_device)
		Timeouts.write('\n' + a_device)
	except (SSHException):
		print ('SSH might not be enabled: ' + a_device)
		SSHException.write('\n' + a_device)
	except (EOFError):
		print ('\n' + 'End of attempting device: ' + a_device)
		EOFError.write('\n' + a_device)
	except unknown_error:
		print ('Some other error: ' + str(unknown_error))

# -----------------------------------------------------------------------
def main():
	"""
	Use threads to run run_commands function.
	Record the amount of time required to do this.
	"""
	start_time = datetime.now()

	for a_device in devices:
		my_thread = threading.Thread(target=run_commands, args=(a_device,))
		my_thread.start()

	main_thread = threading.currentThread()
	for some_thread in threading.enumerate():
		if some_thread != main_thread:
			print(some_thread)
			some_thread.join()

	print("\nElapsed time: " + str(datetime.now() - start_time))

if __name__ == "__main__":
	main()
