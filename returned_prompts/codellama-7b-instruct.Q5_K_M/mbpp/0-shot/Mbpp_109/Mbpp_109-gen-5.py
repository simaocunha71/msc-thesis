"""
def odd_Equivalent(binary_String,n):
    count = 0
    for i in range(n):
        temp = binary_String[-1]
        binary_String = binary_String[:-1] + temp
        if int(temp) % 2 == 1:
            count += 1
    return count
"""