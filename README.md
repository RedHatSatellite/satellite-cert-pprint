# Overview

Script to 'pretty print' a Red Hat Satellite 5 certificate. As a Satellite 5 user,
I work with a LOT of Satellite certificates, and I needed a means to print them out
in a manner more conducive to email/pastebin. 

# Requirements

* Python >= 2.6
* One Satellite 5.x entitlement cert. 

# Usage

~~~
↪ ./satellite-cert-pprint.py -f ~/Megacorp-sat5.cert
~~~

# Help Output

~~~
↪ ./satellite-cert-pprint.py -h
Usage: satellite-cert-pprint.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILENAME, --filename=FILENAME
                        path to Satellite Entitlement certificate
~~~

# Example Output

↪ ./satellite-cert-pprint.py -f ~/Megacorp-sat5.cert
================================================================================
product                                                         MegaCorp - Sat 5
owner                                                                   MEGACORP
issued                                                       2015-10-21 16:27:34
expires                                                      2021-12-31 00:00:00
slots                                                                    1026466
monitoring-slots                                                          525000
provisioning-slots                                                       1026461
virtualization_host                                                        25460
virtualization_host_platform                                               25000
================================================================================
Channel Family                                         Quantity             Flex
================================================================================
rhel-server-7                                            526005           500500
rhel-server-7-eus                                        525003           500000
rhel-server-7-fastrack                                     1001              500
rhel-server-7-ha                                         525966           500500
rhel-server-7-ha-eus                                     525000           500000
rhel-server-7-ha-htb                                     525000           500000
rhel-server-7-htb                                        525000           500000
rhel-server-7-lb                                         525000           500000
rhel-server-7-lb-htb                                     525000           500000
rhel-server-7-optional                                   526001           500500
rhel-server-7-optional-eus                               525000           500000
rhel-server-7-optional-htb                               525000           500000
rhel-server-7-oracle-java                                526003           500500
rhel-server-7-oracle-java-eus                            525003           500000
rhel-server-7-rh-common                                  526001           500500
rhel-server-7-rhgs                                       525003           500000
rhel-server-7-rhgs-bigdata                               525003           500000
rhel-server-7-rhgs-rhsc                                  525003           500000
rhel-server-7-rhscl-1                                    525541           500500
rhel-server-7-rhscl-1-eus                                525000           500000
rhel-server-7-rhsclient                                   20000            10000
rhel-server-7-rs                                         525000           500000
rhel-server-7-rs-eus                                     525000           500000
rhel-server-7-rs-htb                                     525000           500000
rhel-server-7-sap                                        525000           500000
rhel-server-7-v2vwin                                     526001           500500
================================================================================
satellite-version                                                            5.7
generation                                                                     2
================================================================================

