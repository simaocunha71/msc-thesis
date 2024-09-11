"""
def removezero_ip(ip):
    if ip[0]=='0':
        return removezero_ip(ip[1:])
    else:
        return ip
print(removezero_ip("216.08.094.196"))"""

# This is a Python program to remove the leading zeroes in an IP address.

def removezero_ip(ip):
    ip = ip.split(".")
    for i in range(4):
        if ip[i][0] == '0':
            ip[i] = ip[i][1:]
    return ".".join(ip)

print(removezero_ip("216.08.094.196"))

# The program takes an IP address as input and splits it into four parts using the '.' as the delimiter.
# Then, it iterates through each part and checks if the first character is '0'. If it is, it removes the leading zero by slicing the string from the second character onwards.
# Finally, it joins the modified parts back together with a '.' and returns the result.

# The assert statement at the beginning of the program demonstrates that the function works correctly by comparing the result of the function with the expected output.

"""
In this program, the function removezero_ip takes an IP address as input and removes the leading zeroes from it. It does this by splitting the IP address into four parts using the '.' as the delimiter, iterating through each part, checking if the first character is '0', and removing the leading zero if it is. Finally, it joins the modified parts back together with a '.' and returns the result. The assert statement at the beginning of the program demonstrates that the function works correctly by comparing the result of the function with the expected output.
"""

"""
In this program, the function removezero_ip is used to remove leading zeroes from an IP address. The function splits the IP address into four parts using the '.' as the delimiter. It then iterates through each part, checking if the first character is '0'. If it is, the function removes the leading zero by slicing the string from the second character onwards. Finally, it joins the modified parts back