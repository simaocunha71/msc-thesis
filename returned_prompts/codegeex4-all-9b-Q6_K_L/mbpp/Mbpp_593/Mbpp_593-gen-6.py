def removezero_ip(ip_address):
    ip_list = ip_address.split('.')
    ip_list = [str(int(i)) for i in ip_list]
    return '.'.join(ip_list)

