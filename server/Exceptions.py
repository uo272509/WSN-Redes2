class UnregisteredDeviceException(Exception):
    """Exception raised when asking for the ID of an unregistered device

    Attributes:
        ip -- IP of the unregistered device
    """
    def __init__(self, ip):
        self.ip = ip
        super.__init__("Device with ip \"" + ip + "\" is not registered")
