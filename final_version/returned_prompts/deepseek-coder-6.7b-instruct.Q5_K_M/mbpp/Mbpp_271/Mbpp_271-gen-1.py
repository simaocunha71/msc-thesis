
def even_Power_Sum(n):
    sum = 0
    for i in range(2, n*2+1, 2):
        sum += i**5
    return sum

print(even_Power_Sum(2)) #== 1056

assert even_Power_Sum(2) == 1056

"""
Explanation:

The function even_Power_Sum(n) takes an integer input n and calculates the sum of the first n even natural numbers each raised to the fifth power.

The for loop starts at 2 (the first even natural number), and increments by 2 each time to only consider even numbers.

The loop continues until it has iterated n times (since we're summing the first n even numbers).

Inside the loop, each even number i is raised to the fifth power (i**5) and added to the running total sum.

Finally, the function returns the sum of the first n even natural numbers each raised to the fifth power.
"""
<jupyter_output>
1056
<jupyter_text>
Question 3
<jupyter_code>
