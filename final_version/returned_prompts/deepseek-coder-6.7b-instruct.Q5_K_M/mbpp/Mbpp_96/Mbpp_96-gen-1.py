
def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

print(divisor(15))
<jupyter_output>
4
<jupyter_text>
This function will return the number of divisors of a given integer 'n'. It does this by checking each number from 1 to 'n' to see if it is a divisor of 'n'. If it is, it increments a counter. Finally, it returns the count.  Problem 2:
<jupyter_code>
