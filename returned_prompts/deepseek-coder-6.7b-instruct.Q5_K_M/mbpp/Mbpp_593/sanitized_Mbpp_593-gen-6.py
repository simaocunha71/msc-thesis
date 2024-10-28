def removezero_ip(ip):
    l = ip.split('.')
    l = [str(int(i)) for i in l]
    return '.'.join(l)