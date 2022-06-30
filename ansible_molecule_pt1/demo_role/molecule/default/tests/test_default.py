"""Role testing files using testinfra."""

import pytest

# Confirm that specific packages and versions are installed
@pytest.mark.parametrize("name,version", [
    ("epel-release", "8"),
    ("htop", "3.0"),
    ("nginx", "1.14"),
    ("git", "2.31"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)

# Test that the webapp user is available.
@pytest.mark.parametrize("user,group", [
    ("webapp", "webapp"),
])
def test_users(host, user, group):
    usr = host.user(user)
    assert usr.exists
    assert usr.group == group

# Test that app.conf is present and has expected permissions
@pytest.mark.parametrize("filename,owner,group,mode", [
    ("/opt/webapp/app.conf", "webapp", "webapp", 0o755),
])
def test_file(host, filename, owner, group, mode):
    target = host.file(filename)
    assert target.exists
    assert target.user == owner
    assert target.group == group
    assert target.mode == mode
