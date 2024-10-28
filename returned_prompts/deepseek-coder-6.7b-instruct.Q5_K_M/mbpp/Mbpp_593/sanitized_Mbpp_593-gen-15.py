def removezero_ip(ip):
    ip_address = ip.split('.')
    ip_address = [str(int(i)) for i in ip_address]
    return '.'.join(ip_address)