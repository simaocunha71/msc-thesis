
def removezero_ip(ip):
    ip_add = ip.split('.')
    ip_add = [str(int(i)) for i in ip_add]
    return '.'.join(ip_add)


