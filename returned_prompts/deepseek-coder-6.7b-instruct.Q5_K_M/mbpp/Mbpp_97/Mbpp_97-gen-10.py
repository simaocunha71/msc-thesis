def frequency_lists(list_of_lists):
    frequency_dict = {}
    for sub_list in list_of_lists:
        for element in sub_list:
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1
    return frequency_dict

print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))

# Expected output: {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

# Explanation:
# The function `frequency_lists` takes a list of lists as input. 
# It iterates over the sub-lists and then over the elements of each sub-list. 
# If an element already exists in the dictionary, it increments its value by 1. 
# If an element does not exist in the dictionary, it adds it with a value of 1. 
# Finally, it returns the dictionary.
<jupyter_output>
{1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
<jupyter_text>
Question 3
<jupyter_code>
