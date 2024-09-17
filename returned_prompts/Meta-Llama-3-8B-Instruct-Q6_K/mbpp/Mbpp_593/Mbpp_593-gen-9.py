```
def removezero_ip(ip):
    return '.'.join(str(int(x)) for x in ip.split('.'))
```
This function splits the ip address by '.' and then converts each part to an integer. The int() function removes leading zeroes. Finally, it joins the parts back together with '.' in between. 

For example, if the input is "216.08.094.196", the output will be "216.8.94.196". 

The unit test `assert removezero_ip("216.08.094.196")==('216.8.94.196')` ensures that the function works correctly. 
```
```



