def removezero_ip(ip: str) -> str:
    return '.'.join(map(str, [int(i) for i in ip.split('.')]))