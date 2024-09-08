def find_Average_Of_Cube(n):
    total_sum = 0
    for i in range(1, n+1):
        total_sum += i**3
    return total_sum/n

print(find_Average_Of_Cube(2))

# OUTPUT: 4.5

# Explanation: The cube of first 2 natural numbers are 1^3 = 1 and 2^3 = 8. Their average is (1+8)/2 = 4.5.
<jupyter_output>
4.5
<jupyter_text>
3. Write a Python function to find the sum of the digits of a number.
<jupyter_code>
# 