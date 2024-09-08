def sum_of_digits(lst):
    result = []
    for num in lst:
        sum_digits = 0
        while num > 0:
            digit = num % 10
            sum_digits += digit
            num = num // 10
        result.append(sum_digits)
    return result

print(sum_of_digits([10,2,56]))
<jupyter_output>
[1, 2, 11]
<jupyter_text>
Q2. Write a function to compute the product of digits of each number of a given list.
<jupyter_code>
