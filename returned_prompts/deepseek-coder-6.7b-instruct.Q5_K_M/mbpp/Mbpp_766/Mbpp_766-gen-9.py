def pair_wise(lst):
    return [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]


print(pair_wise([1, 1, 2, 3, 3, 4, 4, 5]))

# Output: [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]

"""
Explanation:
The function `pair_wise` takes a list `lst` as input. It creates a list of tuples by iterating over the indices of `lst`. For each index `i`, it takes the pair `(lst[i], lst[i + 1])` and adds it to the list. The pairs are obtained by advancing the index by 1 for each iteration. The loop stops at the second to last index of `lst` because `lst[i + 1]` would be out of range if `i` was the last index. The list of tuples is then returned as the result of the function.
"""

# In the above code, we use list comprehension which is a concise way to create lists in Python. It consists of brackets containing an expression followed by a for statement, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.

# The for statement is what moves over the list, and the if clause is optional and lets you filter out items from the list before it gets added to the new list.

# So, the line `[(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]` is essentially the same as this:

# pairs = []
# for i in range(len(lst) - 1):
#     pairs.append((lst[i], lst[i + 1]))
# return pairs

# In this case, the range function generates numbers from 0 up to (but not including) len(lst) - 1. This is because we want to get pairs of consecutive items, so we need to stop one step before