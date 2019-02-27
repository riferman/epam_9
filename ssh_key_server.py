#!/usr/bin/python

'''Write a module that will create a passwordless connection for a set of Linux machines.
For details see https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys
This means we need to generate an ssh key-pair(s) and distribute it over all the machines supplied.
This can be either a single pair of keys for all machines or each pair distributed over each machine.
Mind the ability of automated clearing ssh key pairs from hosts. *Would be nice to have backup and restore functions.
The set of machine IPs should be taken from a file nearby.
Consider password and login are known in constants, or set in the config file.'''

import os
import json
import paramiko


def ips():
    with open("config.json") as config:
        config_data = json.load(config)
        return config_data


def deploy_key(key, server, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, username=username, password=password, timeout=2)
    client.exec_command('mount -o remount,rw /')
    client.exec_command('mkdir -p ~/.ssh/')
    client.exec_command('echo "%s" > ~/.ssh/authorized_keys' % key)
    client.exec_command('chmod 644 ~/.ssh/authorized_keys')
    client.exec_command('chmod 700 ~/.ssh/')
    client.exec_command('mount -o remount,ro /')
    client.close()


a = ips()
key = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()

for i in a['ips']:
    deploy_key(key, i, a["username"], a["password"])
