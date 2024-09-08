def removezero_ip(ip):
    octets = ip.split('.')
    return '.'.join([str(int(octet)) for octet in octets])

print(removezero_ip("216.08.094.196"))

# Output: 216.8.94.196

# 2. Code:

"""
