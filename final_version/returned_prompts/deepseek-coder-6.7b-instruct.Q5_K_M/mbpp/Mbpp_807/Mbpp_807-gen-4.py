def first_odd(numbers):
    for n in numbers:
        if n % 2 != 0:
            return n
    return None

print(first_odd([1,3,5])) # Should return 1
print(first_odd([2,4,6])) # Should return None
print(first_odd([1,2,3,4,5,6])) # Should return 1

# 1. We define a function named 'first_odd' that accepts a list of numbers.
# 2. We iterate over each number in the list.
# 3. For each number, we check if it's odd by using the modulus operator (%). If the remainder of the division of the number by 2 is not 0, then it's an odd number.
# 4. If we find an odd number, we return it immediately.
# 5. If we go through all the numbers without finding an odd number, we return None.
<jupyter_output>
1
None
1
<jupyter_text>
**Exercise 2**
<jupyter_code>
