def removezero_ip(ip):
    return '.'.join(i.lstrip('0') or '0' for i in ip.split('.'))