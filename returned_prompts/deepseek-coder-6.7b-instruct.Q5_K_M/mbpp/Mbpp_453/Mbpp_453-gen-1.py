
def sumofFactors(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            sum += i
    return sum

print(sumofFactors(18)) # 26

assert sumofFactors(18) == 26
<jupyter_output>
26
<jupyter_text>
Question 2
<jupyter_code>
