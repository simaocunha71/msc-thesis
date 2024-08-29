
def frequency_lists(lst):
    freq_dict = {}
    for sublist in lst:
        for item in sublist:
            if item in freq_dict:
                freq_dict[item] += 1
            else:
                freq_dict[item] = 1
    return freq_dict

print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))  # {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

"""
This function works by iterating over each sublist in the input list, then iterating over each item in the sublist. If the item is already in the dictionary, it increments its count by 1. If it is not in the dictionary, it adds it with a count of 1.
"""
<jupyter_output>
{1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
<jupyter_text>
Question 2
<jupyter_code>
