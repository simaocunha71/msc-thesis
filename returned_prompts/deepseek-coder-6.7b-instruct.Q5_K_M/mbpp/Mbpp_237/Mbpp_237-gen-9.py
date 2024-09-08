
def check_occurences(lst):
    dic = {}
    for tup in lst:
        dic[tup] = dic.get(tup, 0) + 1
    return dic

print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))
<jupyter_output>
{(3, 1): 2, (1, 3): 2, (2, 5): 2, (5, 2): 2, (6, 3): 1}
<jupyter_text>
