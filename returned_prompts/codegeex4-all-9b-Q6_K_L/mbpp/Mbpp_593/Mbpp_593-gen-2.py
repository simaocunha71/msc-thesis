def removezero_ip(ip: str) -> str:
    return '.'.join(map(str, map(int, ip.split('.'))))

