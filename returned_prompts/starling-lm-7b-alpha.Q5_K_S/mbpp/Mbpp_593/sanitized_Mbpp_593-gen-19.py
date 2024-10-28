def removezero_ip(ip: str) -> str:
    while ip[0] == '0':
        ip = ip[1:]
    return ip