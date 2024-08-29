def tuple_to_dict(tup):
    return {tup[i]: tup[i + 1] for i in range(0, len(tup) - 1, 2)}

print(tuple_to_dict((1, 5, 7, 10, 13, 5)))

# Output: {1: 5, 7: 10, 13: 5}

"""
The function `tuple_to_dict` creates a dictionary using dictionary comprehension. It iterates over the tuple in steps of 2 (using `range(0, len(tup) - 1, 2)`), and for each iteration, it sets the key-value pair where the key is the current element (`tup[i]`) and the value is the next element (`tup[i + 1]`).
"""
<jupyter_output>
{1: 5, 7: 10, 13: 5}
<jupyter_text>
Q2. Write a Python program to find the difference between the two lists.
<jupyter_code>
# Program to find the difference between two lists

def list_difference(list1, list2):
    return list(set(list1) - set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8]

print(list_difference(list1, list2))
<jupyter_output>
[1, 3, 5]
<jupyter_text>
Q3. Write a Python program to remove duplicates from a list while preserving the order.
<jupyter_code>
# Program to remove duplicates from a list while preserving the order

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

lst = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5,