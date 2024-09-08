def common_in_nested_lists(nested_lists):
    common_elements = set(nested_lists[0])
    for lst in nested_lists[1:]:
        common_elements = common_elements & set(lst)
    return list(common_elements)

print(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))

# Output: [18, 12]

"""
Explanation:
The function works by first converting the first list into a set of its elements, and then intersects it with the set of the second list's elements. The result of this intersection operation is then used as the new common_elements set for the next list, and the process continues until all of the lists have been processed.
At the end, the result is returned as a list.
"""
<jupyter_output>
[18, 12]
<jupyter_text>
10. Write a function that takes in a string and returns a string with all the vowels removed.
<jupyter_code>
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join([char for char in s if char not in vowels])

print(remove_vowels("Hello, World!"))

# Output: "Hll, Wrld!"
<jupyter_output>
Hll, Wrld
<jupyter_text>
11. Write a function that takes in a list of integers and returns a new list with all duplicate elements removed.
<jupyter_code>
def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5, 6, 6, 7]))

# Output: [1, 2, 3, 4, 