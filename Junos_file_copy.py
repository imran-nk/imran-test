import os
from netmiko import ConnectHandler, file_transfer
from getpass import getpass


hostfile="/Users/mimran/Documents/virtual-env/first/hostfile.txt"
username = 'mimran'
password = getpass()
platform = 'juniper_junos'

source_file = "test.txt"
dest_file = "test.txt"
direction = "put"
file_system= "/var/tmp"


with open(hostfile) as f:
    for line in f:
        host = line.strip()
        ssh_conn = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
        transfer_dict = file_transfer(
            ssh_conn,
            source_file=source_file,
            dest_file=dest_file,
            file_system=file_system,
            direction=direction,
            overwrite_file=True,
        )
        print(transfer_dict)
