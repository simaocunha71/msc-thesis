def removezero_ip(ip_address):
    a, b, c, d = ip_address.split('.')
    return f"{a}.{b}.{c}.{d}"