#!/usr/bin/env python2.7

import paramiko
import time


i=1
ip_address = "10.225.96.85"
username = "admin"
password = "0zzieMan"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()

for n in range(3001,3060):
	if n%2 != 0:
		remote_connection.send("VLAN " + str(n) + "\n")
		remote_connection.send("name VLAN_" + str(n) + "\n")
		remote_connection.send("exit \n")
		remote_connection.send("interface VLAN " + str(n) + "\n")
		remote_connection.send("ip address 11."+ str(i) +".0.1 255.255.0.0" + "\n")
	elif n%2 == 0:
		remote_connection.send("VLAN " + str(n) + "\n")
		remote_connection.send("name VLAN_" + str(n) + "\n")
		remote_connection.send("exit \n")
		remote_connection.send("interface VLAN " + str(n) + "\n")
		remote_connection.send("ip address 12." + str(i) +".0.1 255.255.0.0" + "\n")
		i = i + 1


#    print "Creating VLAN " + str(n)
 #   remote_connection.send("vlan " + str(n) +  "\n")
  #  remote_connection.send("name Python_VLAN " + str(n) +  "\n")
time.sleep(10.0)

remote_connection.send("end\n")

time.sleep(2)
output = remote_connection.recv(65535)
print output

ssh_client.close
