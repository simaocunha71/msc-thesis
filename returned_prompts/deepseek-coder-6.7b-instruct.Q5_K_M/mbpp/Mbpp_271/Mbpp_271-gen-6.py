
def even_Power_Sum(n):
    sum = 0
    for i in range(2, n*2+1, 2):
        sum += i**5
    return sum

print(even_Power_Sum(2))

"""
Explanation:

In the function `even_Power_Sum(n)`, we use a for loop to iterate from 2 to `n*2+1` (in steps of 2), which gives us the first `n` even natural numbers. For each number `i` in the range, we raise `i` to the 5th power (`i**5`), and add that to the `sum`.

Finally, we return `sum`.

In the given assert statement, `even_Power_Sum(2)` is called with the argument 2. This function returns the sum of the cubes of the first 2 even natural numbers (which are 2 and 4), which is 1056. Thus, the assert statement is true.
"""

# Test case 2
# 