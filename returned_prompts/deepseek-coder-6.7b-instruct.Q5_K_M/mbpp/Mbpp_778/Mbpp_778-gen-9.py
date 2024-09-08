def pack_consecutive_duplicates(lst):
    result = []
    i = 0

    while i < len(lst):
        count = 1
        while i + 1 < len(lst) and lst[i] == lst[i + 1]:
            i += 1
            count += 1
        result.append([lst[i]] * count)
        i += 1

    return result

print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))

# Output: [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

"""
Explanation:
The function iterates over the given list. If it finds consecutive duplicates, it counts them and then adds these numbers to the result list in the form of a sublist. 
If it encounters a unique number, it adds this number to the result list as a sublist with one occurrence.
"""
<jupyter_output>
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
<jupyter_text>
