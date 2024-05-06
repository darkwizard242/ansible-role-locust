[![build-test](https://github.com/darkwizard242/ansible-role-locust/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-locust/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-locust/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-locust/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/locust) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-locust&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-locust) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-locust&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-locust) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-locust&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-locust) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-locust?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-locust?color=orange&style=flat-square)

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

Variable                             | Description
------------------------------------ | ------------------------------------------------------------------------------------------------------------------
locust_debian_pre_reqs               | Packages required to install **locust** on Debian based systems. Using python3 as python2.x is EOL by end of 2020.
locust_debian_pre_reqs_desired_state | Desired state for **locust** pre-requisite apps on Debian systems.
pip_executable                       | The executable to utilize for installing **pip** package of `locust`.
locust_app_debian_package            | Name of locust application package require to be installed i.e. `locust` on Debian based systems.
locust_desired_state                 | Desired state for **locust**.

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

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/), a DevOps/CloudOps Engineer who loves to learn and contribute to Open Source community.
