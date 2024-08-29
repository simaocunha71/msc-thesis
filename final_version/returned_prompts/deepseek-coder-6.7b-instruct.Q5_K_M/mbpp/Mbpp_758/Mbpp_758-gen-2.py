def unique_sublists(lst):
    count_dict = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in count_dict:
            count_dict[tuple_sublist] += 1
        else:
            count_dict[tuple_sublist] = 1
    return count_dict

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))
<jupyter_output>
{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
<jupyter_text>
Problem 3:
<jupyter_code>
