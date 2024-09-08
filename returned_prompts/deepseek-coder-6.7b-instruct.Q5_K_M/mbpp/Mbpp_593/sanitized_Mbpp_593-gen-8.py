def removezero_ip(ip):
    octets = ip.split('.')
    return '.'.join([str(int(octet)) for octet in octets])