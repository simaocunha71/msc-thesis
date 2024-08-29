def sumofFactors(num):
    sum = 0
    for i in range(1, num+1):
        if num % i == 0 and i % 2 == 0:
            sum += i
    return sum

print(sumofFactors(18))
assert sumofFactors(18) == 26
<jupyter_output>
26
<jupyter_text>
