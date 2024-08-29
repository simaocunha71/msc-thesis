
def sum_of_digits(lst):
    res = []
    for num in lst:
        sum_digits = 0
        while num > 0:
            digit = num % 10
            sum_digits += digit
            num //= 10
        res.append(sum_digits)
    return res

print(sum_of_digits([10,2,56])) # it should return [1, 2, 11]
<jupyter_output>
[1, 2, 11]
<jupyter_text>
