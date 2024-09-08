
def removezero_ip(ip):
    l = ip.split('.')
    l = [str(int(i)) for i in l]
    return '.'.join(l)

print(removezero_ip("216.08.094.196"))
<jupyter_output>
216.8.94.196
<jupyter_text>
Problem 3
<jupyter_code>
