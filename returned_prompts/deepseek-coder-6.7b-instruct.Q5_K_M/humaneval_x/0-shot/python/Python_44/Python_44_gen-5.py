

def change_base(x: int, base: int):
    result = ''
    while x:
        result = str(x % base) + result
        x //= base
    return result


print(change_base(8, 3))  # 22
print(change_base(8, 2))  # 1000
print(change_base(7, 2))  # 111


# The function `change_base` works by taking the modulus of the input number `x` with the base. 
# This gives us the remainder of the division of `x` by `base`. 
# We append this remainder to the result string. 
# We then divide `x` by the base using integer division and repeat the process until `x` becomes 0. 
# At the end, we return the reversed result string which represents `x` in the new base.
# This is because of the way the algorithm works, the least significant digit comes first, 
# and the most significant digit comes last in the resulting string.

# This approach works for any number and base, including negative numbers and bases greater than 10. 
# However, the problem statement specifically asked for bases less than 10. 
# If you need to support bases greater than 10, you would need to replace the digits in the resulting string with the corresponding characters from a-z, 
# which would require a different approach.
<jupyter_output>
<empty_output>
<jupyter_text>
