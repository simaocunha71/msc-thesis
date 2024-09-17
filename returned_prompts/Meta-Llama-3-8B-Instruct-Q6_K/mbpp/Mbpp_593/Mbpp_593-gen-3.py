```
def removezero_ip(ip):
    return '.'.join(str(int(x)) for x in ip.split('.'))
```
The function takes an IP address as a string, splits it into four parts using the '.' as a separator, converts each part to an integer, removes any leading zeroes, and then joins the parts back together using '.' as a separator. The result is a string representing the IP address with no leading zeroes. 

The unit test `assert removezero_ip("216.08.094.196")==('216.8.94.196')` ensures that the function works correctly. It checks that the output of the function for the input "216.08.094.196" is indeed "216.8.94.196". 

The function uses list comprehension to convert each part of the IP address to an integer and remove leading zeroes. This is a concise and efficient way to achieve the desired result. 

Note that this function assumes that the input is a valid IP address with four parts separated by '.'. If the input is not a valid IP address, the function may not work correctly. 

Also, note that the function returns a string, not a tuple. This is because the problem statement does not specify that the output should be a tuple. If you want the output to be a tuple, you can modify the function to return a tuple instead. 

Finally, the function does not handle IPv6 addresses, which have a different format than IPv4 addresses. If you need to handle IPv6 addresses, you will need to modify the function accordingly. 