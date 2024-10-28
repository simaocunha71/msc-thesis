```
def removezero_ip(ip):
    return '.'.join(map(str, map(int, ip.split('.'))))
```


The function works as follows:
1. `ip.split('.')` splits the ip address into a list of strings, separated by '.'.
2. `map(int, ...)` converts these strings into integers.
3. `map(str, ...)` converts these integers back into strings, so that `join` can concatenate them.
4. `join` concatenates the strings with '.' in between.
5. The result is a new string with the leading zeroes removed. 

Note that this function does not handle invalid ip addresses. If the input is not a valid ip address, the function may return an incorrect result. If you want to handle invalid ip addresses, you would need to add additional error checking code. 

For example, you could add a check to make sure each part of the ip address is between 0 and 255. 

Here is an example of how you could do this:

```
def removezero_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        raise ValueError("Invalid ip address")
    for part in parts:
        if not part.isdigit():
            raise ValueError("Invalid ip address")
        if int(part) < 0 or int(part) > 255:
            raise ValueError("Invalid ip address")
    return '.'.join(map(str, map(int, parts)))
```


This version of the function raises a ValueError if the input is not a valid ip address. It also removes leading zeroes from the ip address. 

The unit test `assert removezero_ip("216.08.094.196")==('216.8.94.196')` will pass with this version of the function. 

Note that this function considers "192.168.0.1" and "192.168.000.1" to be the same ip address. If you want to consider them different, you would need to add additional code to remove trailing zeroes as well. 

Here is an example of how you could do this:

```
def removezero_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        raise ValueError("Invalid ip address")
    for i, part in enumerate(parts):
        if not part.isdigit():
            raise ValueError("Invalid ip address")
        if int(part) < 0 or int(part) > 255:
            raise ValueError("Invalid ip address")
        parts[i] = str(int(part