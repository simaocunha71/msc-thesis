
def recursive_list_sum(lst):
    if lst == []:
        return 0
    elif type(lst[0]) == list:
        return recursive_list_sum(lst[0]) + recursive_list_sum(lst[1:])
    else:
        return lst[0] + recursive_list_sum(lst[1:])

print(recursive_list_sum([1, 2, [3,4],[5,6]]))
<jupyter_output>
21
<jupyter_text>
**Question 3**
<jupyter_code>
