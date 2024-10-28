```
def removezero_ip(ip):
    return '.'.join(str(int(x)) for x in ip.split('.'))
```


The function `removezero_ip` takes an ip address as a string, splits it into four parts, removes leading zeroes from each part, and then joins them back together with '.' in between. The `str(int(x))` is used to remove leading zeroes, because `int('012')` equals `12`. This function passes the given unit test. 





