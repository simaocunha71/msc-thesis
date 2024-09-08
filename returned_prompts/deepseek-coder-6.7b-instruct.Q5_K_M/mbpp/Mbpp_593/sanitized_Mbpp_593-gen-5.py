def removezero_ip(ip):
    ip_split = ip.split('.')
    ip_no_zero = [str(int(i)) for i in ip_split]
    return '.'.join(ip_no_zero)