def sum_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_digits(345))

# 3
# 4
# 5
# 12

# 345의 각 자리 숫자를 더하는 함수를 작성하라.
assert sum_digits(345)==12

# 345의 각 자리 숫자를 더하면 12이므로 True를 반환한다.
assert sum_digits(12345)==15

# 12345의 각 자리 숫자를 더하면 15이므로 True를 반환한다.
<jupyter_output>
<empty_output>
<jupyter_text>
10.2 문제 풀이
<jupyter_code>
