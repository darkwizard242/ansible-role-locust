import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_locust_binary_exists(host):
    assert host.file('/usr/local/bin/locust').exists


def test_locust_binary_file(host):
    assert host.file('/usr/local/bin/locust').is_file


def test_locust_binary_which(host):
    assert host.check_output('which locust') == '/usr/local/bin/locust'
