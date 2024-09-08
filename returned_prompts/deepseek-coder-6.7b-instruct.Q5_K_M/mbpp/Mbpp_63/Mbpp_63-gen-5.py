def max_difference(tuples):
    maximum = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            difference = abs(tuples[i][0] - tuples[j][0])
            if difference > maximum:
                maximum = difference
    return maximum

print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]))
<jupyter_output>
7
<jupyter_text>
Q1.2:
<jupyter_code>
