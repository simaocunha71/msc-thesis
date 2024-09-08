
def count_list(lst):
    count = 0
    for i in lst:
        if type(i) == list:
            count += 1
    return count

print(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]))

"""
Answer:
The function `count_list` takes a list `lst` as input. It initializes a counter `count` to 0. It then iterates over each element `i` in `lst`. If `i` is a list (i.e., if `i` is an instance of the `list` class), it increments `count` by 1. Finally, it returns `count`. 

The output of the `count_list` function is the number of sublists in the input list. In the example given, the function would return 4 because there are four sublists in the input list.
"""
<jupyter_output>
4
<jupyter_text>
6. Write a python function to check whether a given key already exists in a dictionary.
<jupyter_code>
