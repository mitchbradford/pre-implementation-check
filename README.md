# Pre-implementation-check

A multithreaded script for auditing a subnet of network devices prior to performing a network change using Netmiko.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

```
Python 3
Netmiko
```

### Installing

Populate the commands.txt file with the commands you would like the script to run on the network devices.
Note: the first line needs to be 'exit' to exit out of configuration mode on Cisco routers.

```
exit
show ver
show ip int brief
```

## Running the tests

Run run.py

## Version 0.2
Complete rework, added multithreading, streamlined, built in error handling, support for network ranges, etc.

## Version 0.1
Initial Release

## Authors

* **Mitch Bradford** - [Github](https://github.com/mitchbradford)
* **Brett Verney** - [Github](https://github.com/wifiwizardofoz)

## License

This project is licensed under the GNU GPLv3 License.

## Acknowledgments

* Thanks to ktbyers for the netmiko library and threading examples
