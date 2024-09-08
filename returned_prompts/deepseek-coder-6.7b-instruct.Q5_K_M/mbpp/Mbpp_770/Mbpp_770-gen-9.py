def odd_num_sum(n):
    sum = 0
    for i in range(1, n*2, 2):
        sum += i**4
    return sum

print(odd_num_sum(2))
assert odd_num_sum(2) == 82
<jupyter_output>
82
<jupyter_text>
Question 2
<jupyter_code>
