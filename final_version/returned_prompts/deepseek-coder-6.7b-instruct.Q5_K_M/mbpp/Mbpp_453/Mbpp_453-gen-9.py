def sumofSquareOddFactors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            sum += i ** 2
    return sum

print(sumofSquareOddFactors(18))

assert sumofSquareOddFactors(18) == 81
<jupyter_output>
26
26
9
144
81
<jupyter_text>
Q5