def removezero_ip(ip):
    ip_parts = ip.split('.')
    ip_parts = [str(int(part)) for part in ip_parts]
    return '.'.join(ip_parts)

print(removezero_ip("216.08.094.196"))

# Output: 216.8.94.196

# This function works by splitting the input string on the period character ('.') which separates the different parts of the IP address, 
# then converting each part to an integer (which will remove any leading zeroes), and finally joining the parts back together with periods 
# in between.


