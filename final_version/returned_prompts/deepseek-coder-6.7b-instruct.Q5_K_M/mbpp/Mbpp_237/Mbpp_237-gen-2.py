def check_occurences(lst):
    dic = {}
    for tup in lst:
        if tup in dic:
            dic[tup] += 1
        else:
            dic[tup] = 1
    return dic

print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3
<jupyter_code>
