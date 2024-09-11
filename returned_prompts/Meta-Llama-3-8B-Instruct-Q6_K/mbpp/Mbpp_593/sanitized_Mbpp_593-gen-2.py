def removezero_ip(ip):
    return '.'.join(str(int(x)) for x in ip.split('.') if x)  # or using str.lstrip('0') for each part