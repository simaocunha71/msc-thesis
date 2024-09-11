def removezero_ip(ip):
    return '.'.join(str(int(x)) for x in ip.split('.') if x)  # remove leading zeroes and join with '.'