def removezero_ip(ip: str) -> str:
    return '.'.join(map(lambda x: str(int(x)), ip.split('.')))