def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

print(divisor(15))

#Output: 4

#Explanation: The divisors of 15 are 1, 3, 5, and 15. So the function returns 4.
<jupyter_output>
4
<jupyter_text>
