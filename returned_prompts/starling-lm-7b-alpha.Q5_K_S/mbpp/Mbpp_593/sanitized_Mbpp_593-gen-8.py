def removezero_ip(ip):
    ip = ip.split('.')
    ip = [i for i in ip if i != '00']
    return '.'.join(ip)