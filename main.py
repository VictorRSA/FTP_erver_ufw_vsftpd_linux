#step1: Installing VsFTP Server in Ubuntu
#Very secure File Transfer Protocol Daemon
#substep1:
#secure the machine so that other computer noded mchaine can senet packets od data

#Ubuntu firewall setup

#uncomplicated firewall iptables firewall netfilter as werolling -the firewall as cli for
# controling firewall

#seubstep2 : lets check if ufw is alll $sudo dpkg --get-selections | grep uwf
#substep3: check if ufw is running? inactive
#substep: sudo ufw enableb
#>>>>>Firewall is active and enabled
#to disable is to use:sudo ufw  disable
#lets check default firewall rules: sudo ufw satus verbose
#>>>Status: active
# Logging: on (low)
# Default: deny (incoming), allow (outgoing), disabled (routed)
"""

How to Add ufw rules
"""

# / etc / default / ufw: The
# main
# configuration
# for default policies, IPv6 support and kernel modules.
# / etc / ufw / before[6].rules: rules in these
# files
# are
# calculate
# before
# any
# rules
# added
# via
# the
# ufw
# command.
# / etc / ufw / after[6].rules: rules in these
# files
# are
# calculate
# after
# any
# rules
# added
# via
# the
# ufw
# command.
# / etc / ufw / sysctl.conf: kernel
# network
# tunables.
# / etc / ufw / ufw.conf: sets
# whether or not ufw is enabled
# on
# boot and sets
# the
# LOGLEVEL.
#ADVANCE UFW FUNCTIONALITY

"""
As you see, by default every incoming connection is denied.
If you want to remote your machine then you have to allow proper port.
For example you want to allow ssh connection. Here’s the command to allow it.
"""
#sudo allow ufw 1000/2000udp
#removing rules:sudo ufw delete 1000:2000tcp
#sudo ufw default deny incoming
#Protocal:Port:22/tcp
#sudo ufw allow 21/tcp
#sudo ufw allow www(80/tcp)   #sudo ufw deny 80/tcp
#sudo ufw allow ssh added rule to
#sudo ufw reset cloud server rules
"""
The first rule says that incoming connection to port 22 from Anywhere, 
both tcp or udp packets is allowed. 
What if you want to allow tcp packet only
? Then you can add the parameter tcp after the port number. 
Here’s an example with sample output.
"""
