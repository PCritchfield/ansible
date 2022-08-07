"""Role testing files using testinfra."""

import pytest
import testinfra.utils.ansible_runner
import os

# testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
#     os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts('site')

testinfra_hosts = ["site"]

def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_running_and_enabled(host):
     nginx = host.service("nginx")
     assert nginx.is_running
     assert nginx.is_enabled 
