hf2k13
======

Hackfest 2013 War Game and CTF challenges, tools, sources, etc.

## OpenVPN script
Those script are available in wargame/CA_OpenVPN. If you want to easily
setup an OpenVPN server, from the creation of certificates to pushing
all configuration file to your server, this is the way! Note that in the
case of the Hackfest 2013 games, there was 8 teams so the script is
build accordingly

### Step by step guide
#### .cnf files
First thing you want to do is to setup your configuration file properly.
To do so, go into CA_OpenVPN/files and edit ca.cnf and ca-sign.cnf to
reflect the requirement of your setup.

#### install_config_OpenVPN.sh
This is the first script you want to run. Initialy, it will install
OpenSSL on your system. In the second step, it will call
create_ssl_key.sh script to create the root CA and create all the
required file (crt, key, pem, etc) to use with your OpenVPN server.

#### create_ssl_key.sh
Using OpenSSL, this script replicate the one already given with OpenVPN
(EasyRSA). Why are we doing this? To get a better understanding of the
underlying security, to permit more flexibility and, for fun ;).

Based on the cnf file you (already) have modified, this script will
create the folder structure, CA certificate, Diffie-Hellman challenge
key and the (signed) key for the OpenVPN server of each teams. 

#### create_new_client.sh
Script to create new client certificate for one or all team at once
****Coming soon

#### push_to_team.sh
Script that install OpenVPN on team, then push certificate and
configuration file on each of them
****Coming soon
