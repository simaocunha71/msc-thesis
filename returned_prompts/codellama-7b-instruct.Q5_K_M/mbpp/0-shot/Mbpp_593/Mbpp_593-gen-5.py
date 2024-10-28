def removezero_ip(ip_address):
    list_ip = ip_address.split('.')
    for i in range(len(list_ip)):
        while list_ip[i][0] == '0':
            list_ip[i] = list_ip[i][1:]
    return '.'.join(list_ip)

