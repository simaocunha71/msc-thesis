def removezero_ip(ip):
    ip_parts = ip.split('.')
    ip_parts = [str(int(part)) for part in ip_parts]
    return '.'.join(ip_parts)

print(removezero_ip("216.08.094.196"))


