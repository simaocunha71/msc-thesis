"""
def removezero_ip(ip):
    ip=ip.split('.')
    ip=[str(x) for x in ip if x!='0']
    return '.'.join(ip)

print(removezero_ip("216.08.094.196"))
"""

