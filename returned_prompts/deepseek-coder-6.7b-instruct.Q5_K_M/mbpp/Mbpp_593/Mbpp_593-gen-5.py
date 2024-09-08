def removezero_ip(ip):
    ip_split = ip.split('.')
    ip_no_zero = [str(int(i)) for i in ip_split]
    return '.'.join(ip_no_zero)

print(removezero_ip("216.08.094.196"))
<jupyter_output>
216.8.94.196
<jupyter_text>
10. Write a Python program to create a list containing tuples. Each tuple contains the name of an item and its price. You need to sort the list by the price and then alphabetically by name.
<jupyter_code>
