def removezero_ip(ip_address: str) -> str:
    octets = ip_address.split('.')
    return '.'.join([str(int(o)) for o in octets])