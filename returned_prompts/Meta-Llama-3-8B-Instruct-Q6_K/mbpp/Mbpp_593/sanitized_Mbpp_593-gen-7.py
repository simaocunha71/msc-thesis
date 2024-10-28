def removezero_ip(ip):
    return '.'.join(str(int(x)) for x in ip.split('.') if x != '0') or '0.0.0.0'