def removezero_ip(ip):
    ip = ip.split('.')
    for i in range(len(ip)):
        if len(ip[i]) == 0:
            ip[i] = '0'
    return ".".join(ip)