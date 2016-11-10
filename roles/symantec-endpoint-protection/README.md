symantec-endpoint-protection
=========

A role that installs the Install Symantec Endpoint Protection Agent

Requirements
------------

The SEP tar file must be accessible over the network

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

```
# The network location of the SEP tarball.
remote_src: http://myserver.com/pub/SEP-1216.tar
```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: symantec-endpoint-protection, remote_src: http://myserver.com/pub/SEP-1216.tar }

License
-------

BSD

Author Information
------------------

Written by Caitlin Campbell for USCBP
