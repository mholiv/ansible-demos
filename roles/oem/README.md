Oracle Enterprise Manager Agent Deployment Role
===============================================

Red Hat Notes
-------------
This role has been inspected for malicious code by Caitlin Campbell.
[cacampbe@redhat.com](mailto:cacampbe@redhat.com)

The [dareko.emagent](https://galaxy.ansibleworks.com/list#/roles/290) role deploys the Oracle Enterprise Manager agent on a target host.
It requires the Oracle Enterprise Manager agent image to be provided by the user.

The oinstall group and the oracle account are created by the role if they don't exist.

Requirements
------------

This role requires Ansible 1.4 or higher and Oracle Enterprise Manager 12c.
Platform requirements are listed in the Supported Platforms section of the role details.

Oracle Enterprise Manager agent image need to be prepared separately by executing
the following command and copying the agent image to the `files` directory.

    emcli get_agentimage -platform="Linux x86-64" -version=12.1.0.3.0 -destination=/tmp

See the Oracle Enterprise Manager documentation for details.

Role Variables
--------------

The variables that can be passed to this role with default values are as follows.

    # version
    emagent_version: 12.1.0.3.0

    # installation base directory
    emagent_base: /opt/oracle

    # installation directory
    emagent_dir: agent12c

    # port for emagent
    emagent_port: 3872

    # OMS host
    emagent_oms_host:

    # OMS upload host
    emagent_oms_port: 1159

    # OMS agent registration password
    emagent_oms_password:

    # list of dependencies
    emagent_packages:
      - bc
      - setarch

See the Oracle Enterprise Manager documentation for details.

Dependencies
------------

None

Example Playbook
----------------

1. Add a group to the `hosts` inventory file

        [emagent]
        host.domain

2. Add variables to the `group_vars/all` file

        emagent_version: 12.1.0.2.0
        emagent_base: /u01/app/oracle/product
        emagent_port: 1830
        emagent_oms_host: oms.domain
        emagent_oms_port: 1159
        emagent_oms_password: agent_registration_password

3. Add role to the `site.yml` file

        - hosts: emagent
          sudo: true
          roles:
          - role: dareko.emagent

4. Run the `site.yml` playbook

        ansible-playbook -i hosts site.yml

License
-------

[MIT License](http://choosealicense.com/licenses/mit/)

Author Information
------------------

[Darek Owczarek](https://galaxy.ansibleworks.com/list#/users/1102)
