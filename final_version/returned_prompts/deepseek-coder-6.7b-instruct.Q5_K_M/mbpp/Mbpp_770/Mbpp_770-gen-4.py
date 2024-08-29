def odd_num_sum(n):
    sum = 0
    num = 1
    for i in range(n):
        sum += num**4
        num += 2
    return sum

print(odd_num_sum(2))
<jupyter_output>
82
<jupyter_text>
Question 4:
<jupyter_code>
