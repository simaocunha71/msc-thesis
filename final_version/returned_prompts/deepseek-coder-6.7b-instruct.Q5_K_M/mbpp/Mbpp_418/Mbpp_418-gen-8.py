def Find_Max(lst):
    max_len = max(len(sub_list) for sub_list in lst)
    max_sub_list = [sub_list for sub_list in lst if len(sub_list) == max_len]
    return max_sub_list[0]

print(Find_Max([['A'],['A','B'],['A','B','C']])) # ['A','B','C']

# This function works by first finding the length of the longest sub-list in the given list (max_len).
# It then creates a new list of sub-lists that have this length (max_sub_list).
# Finally, it returns the first element from this list (since we're looking for the longest sub-list).
<jupyter_output>
['A', 'B', 'C']
<jupyter_text>
