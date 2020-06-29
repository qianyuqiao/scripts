from netaddr import *
ip = IPAddress(value)
if ip.is_unicast() and not ip.is_private():
    return True
