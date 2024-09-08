def cal_sum(n):
    perrin = [3, 0, 2]
    for i in range(3, n+1):
        perrin.append(perrin[i-2] + perrin[i-3])
    return sum(perrin[:n+1])

print(cal_sum(9))
<jupyter_output>
49
<jupyter_text>
