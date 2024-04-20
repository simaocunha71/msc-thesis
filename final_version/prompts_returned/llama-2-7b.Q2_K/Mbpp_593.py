"""
Write a function to remove leading zeroes from an ip address.
assert removezero_ip("216.08.094.196")==('216.8.94.196')
"""

def removezero_ip(ip):
    ip = ip[:-str(len(ip))+1]   #remove leading zero 
    if ip[str(0)] == '0':         #check for a leading zero in the IP address
        return str(int('0'.join([chr(i) for i in ip.split('.')])+128)*-1)[:ip.count('.')]   
    else:                         
        return ip             

#print(removezero_ip("255.08.094.196"))
print(removezero_ip("123.08.094.196"))