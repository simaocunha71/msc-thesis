def count_Set_Bits(n):
    return bin(n).count('1')

print(count_Set_Bits(2))

# or using bit manipulation
def count_Set_Bits(n):
    count = 0
    while n:
        count += n % 2
        n >>= 1
    return count

print(count_Set_Bits(2))

# or using the built-in function
def count_Set_Bits(n):
    return n.bit_count()

print(count_Set_Bits(2))

# or using the format function
def count_Set_Bits(n):
    return format(n, 'b').count('1')

print(count_Set_Bits(2))

# or using a list comprehension
def count_Set_Bits(n):
    return sum([int(i) for i in list(bin(n)[2:])])

print(count_Set_Bits(2))

# or using a for loop
def count_Set_Bits(n):
    count = 0
    for i in bin(n)[2:]:
        if i == '1':
            count += 1
    return count

print(count_Set_Bits(2))

"""
Explanation:
The function count_Set_Bits takes an integer n as an argument. It converts the integer to binary using the bin() function, counts the number of 1's in the binary representation using the count() method, and returns the count.
"""

# or using a while loop
def count_Set_Bits(n):
    count = 0
    while n:
        if n % 2:
            count += 1
        n //= 2
    return count

print(count_Set_Bits(2))
<jupyter_output>
1
1
1
1
1
1
1
<jupyter_text>
