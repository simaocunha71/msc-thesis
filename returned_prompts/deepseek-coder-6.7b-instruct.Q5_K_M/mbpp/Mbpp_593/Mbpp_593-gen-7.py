def removezero_ip(ip):
    ip_list = ip.split('.')
    new_ip_list = [str(int(i)) for i in ip_list]
    new_ip = '.'.join(new_ip_list)
    return new_ip

print(removezero_ip("216.08.094.196"))
<jupyter_output>
216.8.94.196
<jupyter_text>
Question 2
<jupyter_code>
