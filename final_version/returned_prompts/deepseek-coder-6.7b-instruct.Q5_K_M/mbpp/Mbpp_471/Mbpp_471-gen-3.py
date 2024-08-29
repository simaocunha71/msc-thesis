def find_remainder(arr, n):
    product = 1
    for num in arr:
        product = (product * num) % n
    return product

print(find_remainder([ 100, 10, 5, 25, 35, 14 ], 11)) # Output: 9


"""
Explanation:

In the given array [100, 10, 5, 25, 35, 14], if we multiply all the elements together and then find the remainder when divided by n (in this case 11), we get the result 9. 

This is because: 
100 * 10 * 5 * 25 * 35 * 14 = 183000, and 183000 modulo 11 = 9.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2
<jupyter_code>
