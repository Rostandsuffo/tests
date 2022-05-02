from netmiko import ConnectHandler


class SSHConnection(object):
    def __init__(self, device_type, host, port, username, password):
        self.device_type = device_type
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.cli: ConnectHandler = self._get_connection()
