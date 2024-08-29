
def is_samepatterns(lst1, lst2):
    return lst1 == [x for i, x in enumerate(lst2) for _ in range(lst1.index(x)+1 if x in lst1[:i] else 1)]

print(is_samepatterns(["red","green","green"], ["a", "b", "b"]))
"""
Explanation:

The function takes two lists as input. It generates a new list by iterating over the second list and repeating the elements based on the index of the occurrence of the element in the first list. The function then checks if the generated list is the same as the second list. If it is, the function returns True, else it returns False.

In the given example, the function generates the following list: ["a", "b", "b"]. This is the same as the second list: ["a", "b", "b"], so the function returns True.
"""
<jupyter_output>
True
<jupyter_text>
