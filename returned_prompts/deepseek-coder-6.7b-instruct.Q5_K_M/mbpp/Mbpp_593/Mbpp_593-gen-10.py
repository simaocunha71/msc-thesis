def removezero_ip(ip_address):
    ip_parts = ip_address.split('.')
    new_ip_parts = [str(int(part)) for part in ip_parts]
    new_ip_address = '.'.join(new_ip_parts)
    return new_ip_address

print(removezero_ip("216.08.094.196"))

# Output: 216.8.94.196

"""
Explanation:
The function removezero_ip takes an IP address as a string, splits it into its constituent parts by '.', converts each part into an integer,
removes leading zeroes (if any), converts it back to a string and then joins them back together with '.'. This way, leading zeroes are removed from the IP address.
"""
<jupyter_output>
216.8.94.196
<jupyter_text>
Question 2
<jupyter_code>
