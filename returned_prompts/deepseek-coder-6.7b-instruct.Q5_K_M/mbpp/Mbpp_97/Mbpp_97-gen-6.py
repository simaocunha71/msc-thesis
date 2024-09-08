"""
We will use python dictionary to solve this problem.

1. First we will flatten the list of lists.
2. Then we will iterate over the flattened list.
3. For each element in the flattened list, we will increment its count in the dictionary.
4. Finally, we will return the dictionary.
"""

def frequency_lists(lst):
    flat_list = [item for sublist in lst for item in sublist]
    freq = {}
    for item in flat_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))
"""
output:
{1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""
"""
The solution works by first flattening the list of lists. Then it creates a dictionary and for each element in the flattened list, it increments the count in the dictionary. The dictionary is then returned.
"""
<jupyter_output>
{1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
<jupyter_text>
Q2
<jupyter_code>
"""
