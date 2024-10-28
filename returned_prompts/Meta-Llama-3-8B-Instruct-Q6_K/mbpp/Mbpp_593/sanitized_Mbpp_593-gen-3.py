def removezero_ip(ip):
    return '.'.join(str(int(x)) for x in ip.split('.') if x)  # or use str(x).lstrip('0') if you want to keep '0' if there is no other digit after it