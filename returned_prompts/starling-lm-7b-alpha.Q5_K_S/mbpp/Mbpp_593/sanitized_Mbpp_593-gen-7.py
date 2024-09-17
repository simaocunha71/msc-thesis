def removezero_ip(ip):
    ip = ip.split(".")
    for i in range(4):
        if ip[i][0] == '0':
            ip[i] = ip[i][1:]
    return ".".join(ip)