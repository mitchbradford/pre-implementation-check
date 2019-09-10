# Pre-implementation-check

A multithreaded script for auditing a subnet of network devices prior to performing a network change using Netmiko.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

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

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to ktbyers for the netmiko library and threading examples