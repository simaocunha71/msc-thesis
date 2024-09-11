def removezero_ip(ip):
    ip=list(ip)
    for i in range(len(ip)):
        if ip[i]=='0':
            del ip[i]
            i-=1
    ip=''.join(ip)
    return ip

# Another way to remove leading zeroes is by using replace method:
def removezero_ip_2(ip):
    return ip.replace('0.','.')

# Testing the functions
assert removezero_ip("216.08.094.196")==('216.8.94.196')
print("First function is working properly.")
assert removezero_ip_2("216.08.094.196")==('216.8.94.196')
print("Second function is working properly.")
"""
The above code consists of two functions to remove the leading zeroes from an ip address:

1. removezero_ip(ip): This function first converts the ip address to a list of characters. Then, it iterates over each element in the list and if the element is zero, it deletes the element and the previous element. This is done by decrementing the index by one. Finally, it joins the elements of the list to form a string and returns it.

2. removezero_ip_2(ip): This function directly replaces all zeroes with an empty string in the ip address.

Both functions are tested using the assert statement and print statement to check if they are working correctly.
"""

# Another way to remove leading zeroes is by using replace method:
def removezero_ip_2(ip):
    return ip.replace('0.','.')

# Testing the functions
assert removezero_ip("216.08.094.196")==('216.8.94.196')
print("First function is working properly.")
assert removezero_ip_2("216.08.094.196")==('216.8.94.196')
print("Second function is working properly.")
"""
The above code consists of two functions to remove