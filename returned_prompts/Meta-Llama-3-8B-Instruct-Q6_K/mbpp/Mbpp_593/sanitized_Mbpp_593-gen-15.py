def removezero_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        raise ValueError("Invalid IP address")
    for part in parts:
        if not part.isdigit():
            raise ValueError("Invalid IP address")
        if int(part) > 255:
            raise ValueError("Invalid IP address")
    return '.'.join(str(int(part)) for part in ip.split('.'))