"""Role testing files using testinfra."""

testinfra_hosts = ["mysql"]

def test_mysql_is_installed(host):
    mysql = host.package("mysql-server")
    assert mysql.is_installed

def test_mysql_running_and_enabled(host):
     mysql = host.service("mysql")
     assert mysql.is_running
     assert mysql.is_enabled 
