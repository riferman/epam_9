# epam_9

Write a module that will create a passwordless connection for a set of Linux machines.

For details see https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys

This means we need to generate an ssh key-pair(s) and distribute it over all the machines supplied.

This can be either a single pair of keys for all machines or each pair distributed over each machine.

Mind the ability of automated clearing ssh key pairs from hosts. *Would be nice to have backup and restore functions.

The set of machine IPs should be taken from a file nearby. Consider password and login are known in constants, or set in the config file.

 

Use VirtualBox machines for testing, setup network as provided in the article http://rus-linux.net/MyLDP/vm/VirtualBox-networking.html

 

Use paramiko for remote commands execution http://docs.paramiko.org/en/2.4

https://www.adampalmer.me/iodigitalsec/2014/11/23/ssh-sftp-paramiko-python

 

Use subprocess for local commands execution https://docs.python.org/2/library/subprocess.html

https://python-scripts.com/subprocess

 

Perform as many checks as possible to ensure your operations are successful.
