[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-locust.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-locust) ![Ansible Role](https://img.shields.io/ansible/role/49193?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/49193?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/49193?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-locust&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-locust) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-locust?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-locust?color=orange&style=flat-square)

# Ansible Role: locust

Role to install [locust](https://locust.io) pip package on **Debian/Ubuntu** systems for load testing purposes.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
locust_debian_pre_reqs:
  - python3
  - python3-pip
locust_debian_pre_reqs_desired_state: present
pip_executable: pip3
pip_upgrade_version: latest
locust_app_debian_package: locust
locust_desired_state: present
```

### Variables table:

Variable                             | Value (default)      | Description
------------------------------------ | -------------------- | ---------------------------------------------------------------------------------------------------------------
locust_debian_pre_reqs               | python3, python3-pip | Packages required to install AWS CLI on Debian based systems. Using python3 as python2.x is EOL by end of 2020.
locust_debian_pre_reqs_desired_state | present              | Desired state for AWS CLI pre-requisite apps on Debian systems.
pip_executable                       | pip3                 | The executable to utilize for installing **pip** package of `locust`.
locust_app_debian_package            | locust               | Name of locust application package require to be installed i.e. `locust` on Debian based systems.
locust_desired_state                 | present              | Desired state for AWS CLI.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **locust** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.locust
```

For customizing behavior of role (i.e. installation of latest **locust** package instead of ensure it is installed ) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.locust
  vars:
    locust_desired_state: latest
```

For customizing behavior of role (i.e. removal of **locust** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.locust
  vars:
    locust_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-locust/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/), a DevOps/CloudOps Engineer who loves to learn and contribute to Open Source community.
