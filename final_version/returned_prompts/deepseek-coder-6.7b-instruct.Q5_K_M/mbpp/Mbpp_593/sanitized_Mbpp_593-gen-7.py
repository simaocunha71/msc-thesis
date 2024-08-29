def removezero_ip(ip):
    ip_list = ip.split('.')
    new_ip_list = [str(int(i)) for i in ip_list]
    new_ip = '.'.join(new_ip_list)
    return new_ip