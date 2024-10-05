
def total_match(lst1, lst2):
    sum_lst1 = sum([len(i) for i in lst1])
    sum_lst2 = sum([len(i) for i in lst2])
    
    if sum_lst1 < sum_lst2:
        return lst1
    elif sum_lst1 > sum_lst2:
        return lst2
    else:
        return lst1

print(total_match([], []))
print(total_match(['hi', 'admin'], ['hI', 'Hi']))
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))
print(total_match(['4'], ['1', '2', '3', '4', '5']))
<jupyter_output>
[]
['hI', 'Hi']
['hi', 'admin']
['hI', 'hi', 'hi']
['4']
<jupyter_text>
Q2:
<jupyter_code>
