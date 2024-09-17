
def removezero_ip(ip):
    octets = ip.split('.')
    return '.'.join([o for o in octets if o != '0'])


