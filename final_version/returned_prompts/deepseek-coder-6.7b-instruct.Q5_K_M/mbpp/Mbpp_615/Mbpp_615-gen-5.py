def average_tuple(t):
    avg = []
    for i in t:
        avg.append(sum(i)/len(i))
    return avg

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))
<jupyter_output>
[30.5, 34.25, 27.0, 23.25]
<jupyter_text>
Exercise 1.4:
<jupyter_code>
