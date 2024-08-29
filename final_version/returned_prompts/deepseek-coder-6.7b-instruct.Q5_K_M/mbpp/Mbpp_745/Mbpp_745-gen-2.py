
def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum+1):
        if all(i % int(digit) == 0 for digit in str(i) if digit != '0'):
            result.append(i)
    return result

print(divisible_by_digits(1,22))

#output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
<jupyter_output>
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
<jupyter_text>
Question 2:
<jupyter_code>
