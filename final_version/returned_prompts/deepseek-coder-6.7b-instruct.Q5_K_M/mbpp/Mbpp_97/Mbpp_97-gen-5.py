def frequency_lists(lists):
    freqs = {}
    for sublist in lists:
        for item in sublist:
            if item in freqs:
                freqs[item] += 1
            else:
                freqs[item] = 1
    return freqs

assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""
In the function above, we first initialize an empty dictionary freqs. Then we loop over each sublist in the input list. For each sublist, we loop over each item in the sublist and increment its count in the freqs dictionary. If the item is not yet in the dictionary, we add it with a count of 1. Finally, we return the freqs dictionary.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
7. Write a Python function to check if a given key already exists in a dictionary.
<jupyter_code>
