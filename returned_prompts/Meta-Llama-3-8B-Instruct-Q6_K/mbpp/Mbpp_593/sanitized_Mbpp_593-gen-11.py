def removezero_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        raise ValueError("Invalid ip address")
    for part in parts:
        if not part.isdigit():
            raise ValueError("Invalid ip address")
        if int(part) < 0 or int(part) > 255:
            raise ValueError("Invalid ip address")
    return '.'.join(map(str, map(int, parts)))