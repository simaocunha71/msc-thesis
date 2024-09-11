"""


def removezero_ip(str):
    if str[0]=='0':
        return removezero_ip(str[1:])
    else:
        return str

print(removezero_ip("216.08.094.196"))
"""


def removezero_ip(ip):
    ip = ip.split('.')
    for i in range(len(ip)):
        if len(ip[i]) == 1:
            ip[i] = '0' + ip[i]
    return '.'.join(ip)

print(removezero_ip("216.08.094.196"))
"""

def removezero_ip(ip):
    ip = ip.strip('0')
    return ip

print(removezero_ip("216.08.094.196"))
"""

def removezero_ip(ip):
    ip = ip.strip('0')
    ip = ip.replace('0.', '.')
    return ip

print(removezero_ip("216.08.094.196"))
"""

def removezero_ip(ip):
    ip_list = list(ip)
    if ip_list[0] == '0':
        del ip_list[0]
    ip_list = [ip_list[i] for i in range(len(ip_list)) if ip_list[i] != '0']
    return '.'.join(ip_list)

print(removezero_ip("216.08.094.196"))
"""

def removezero_ip(ip):
    ip = ip.strip('0')
    ip = ip.replace('0.', '.')
    return ip

print(removezero_ip("216.08.094.196"))
"""

def removezero_ip(ip):
    ip_list = list(ip)
    if ip_list[0] == '0':
        del ip_list[0]
    ip_list = [ip_list[i] for i in