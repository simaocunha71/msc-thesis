def find_tuples(tuples, k):
    result = []
    for t in tuples:
        if all(i % k == 0 for i in t):
            result.append(t)
    return result

print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))
<jupyter_output>
[(6, 24, 12)]
<jupyter_text>
Question 2
<jupyter_code>
