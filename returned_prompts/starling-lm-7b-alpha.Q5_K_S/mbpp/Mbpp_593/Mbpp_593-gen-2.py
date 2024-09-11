"""
def removezero_ip(ip):
    return ip.replace('00', '').replace(' 0', ' ').replace('  ', ' ').replace(' 0', ' ').replace('  ', ' ').replace(' 0', ' ')


"""

def removezero_ip(ip):
    ip = ip.replace(' 0', ' ').replace('  ', ' ').replace(' 0', ' ').replace('  ', ' ').replace(' 0', ' ')
    return ip.replace('00', '').replace(' 0', ' ').replace('  ', ' ').replace(' 0', ' ').replace('  ', ' ').replace(' 0', ' ')

# removezero_ip("216.08.094.196")
print(removezero_ip("216.08.094.196"))


"""
def removezero_ip(ip):
    ip_list = ip.split('.')
    ip_list_new = [i for i in ip_list if i != '00' and i != ' 0']
    return '.'.join(ip_list_new)
"""

# removezero_ip("216.08.094.196")
print(removezero_ip("216.08.094.196"))


"""
def removezero_ip(ip):
    ip_list = ip.split('.')
    ip_list_new = [i.replace('00', '') for i in ip_list]
    return '.'.join(ip_list_new)
"""

# removezero_ip("216.08.094.196")
print(removezero_ip("216.08.094.196"))


"""
def removezero_ip(ip):
    ip_list = ip.split('.')
    ip_list_new = []
    for i in ip_list:
        if i != '00':
            ip_list_new.append(i)
    return '.'.join(ip_list_