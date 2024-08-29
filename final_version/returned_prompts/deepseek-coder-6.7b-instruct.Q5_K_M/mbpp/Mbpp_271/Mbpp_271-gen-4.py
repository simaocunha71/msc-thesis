def even_Power_Sum(n):
    sum = 0
    for i in range(2, n*2+1, 2):
        sum += i**3
    return sum

print(even_Power_Sum(2))  # 104

"""
Explanation:
The function `even_Power_Sum(n)` is calculating the sum of the third power of the first 'n' even natural numbers. 
The `for` loop runs from 2 to `2*n+1` with a step of 2, so it is getting the first 'n' even numbers. 
For each even number 'i', it is raising it to the power of 3 and adding it to the running total 'sum'. 
Finally, it returns the 'sum'.
"""
<jupyter_output>
104
<jupyter_text>
Q3:
<jupyter_code>
"""
Write a python function that takes in a string and returns the number of vowels in the string.
assert vowel