import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_BINARY = '/usr/local/bin/locust'


def test_locust_binary_exists(host):
    """
    Tests if locust binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_locust_binary_file(host):
    """
    Tests if locust binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_locust_binary_which(host):
    """
    Tests the output to confirm locust's binary location.
    """
    assert host.check_output('which locust') == PACKAGE_BINARY
