def removezero_ip(ip):
    return ('.'.join(map(str,
                         [int(i) for i in ip.split('.')])))
