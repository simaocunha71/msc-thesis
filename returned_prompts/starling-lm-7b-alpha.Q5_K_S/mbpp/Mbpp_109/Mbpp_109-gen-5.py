"""
def odd_Equivalent(str,k):
    odd_count = 0
    for i in range(k):
        str = str[-1]+str[:-1]
        if str[-1] == '1':
            odd_count += 1
    return odd_count
print(odd_Equivalent("011001",6))
"""

