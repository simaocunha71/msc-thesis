def Find_Max(list_items):
    max_len = -1
    max_item = []
    for item in list_items:
        if len(item) > max_len:
            max_len = len(item)
            max_item = item
    return max_item

#Testing the function
print(Find_Max([['A'],['A','B'],['A','B','C']]))
<jupyter_output>
['A', 'B', 'C']
<jupyter_text>
Q2.
<jupyter_code>
