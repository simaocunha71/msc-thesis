def removezero_ip(ip):
    return '.'.join(map(str, map(int, ip.split('.'))))