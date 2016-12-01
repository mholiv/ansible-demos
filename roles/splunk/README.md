splunk_agent_install
=========

Installs the Splunk agent.

Vetted on test env

Requirements
------------

The `splunkforwarder` package must be available in a yum repo.

Role Variables
--------------

```
# The splunk admin password
splunk_admin_password: changeme

# The location of the gpg key for the splunk repo
splunk_rpm_key: http://satellite.mydomain.com/mykey

# The splunk host location
splunk_host: splunkhost.mydomain.com
```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - roles/splunk_agent_install

License
-------

BSD

Author Information
------------------

Written by Caitlin Campbell for USCBP
