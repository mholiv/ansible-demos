nessus
=========

Installs the nessus agent.

Requirements
------------

None

Role Variables
--------------

```
# The nessus key
- nessus_key: NESSUS_KEY_HERE

# The nessus host
- nessus_host: MYHOSTHERE

# The nessus repo gpg key location
- nessus_rpm_key: http://satellite.mydomain.com/mykey

```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role/nessus

License
-------

BSD

Author Information
------------------

Written by Caitlin Campbell for USCBP
