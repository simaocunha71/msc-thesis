```
def removezero_ip(ip):
    return '.'.join(str(int(part)) for part in ip.split('.'))
```
The provided function `removezero_ip` takes an IP address as a string, splits it into four parts, removes any leading zeroes from each part, and then joins the parts back together with '.' in between. It does this by first splitting the IP address into parts using the '.' as a separator, then using a generator expression to convert each part to an integer and remove any leading zeroes, and finally joining the parts back together with '.' in between. This results in an IP address with no leading zeroes. For example, if the input is "216.08.094.196", the output will be "216.8.94.196".