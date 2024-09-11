def combinations_list(lst):
    """
    :type lst: List[str]
    :rtype: List[List[str]]
    """
    res = [[]]
    for i in lst:
        res += [j + [i] for j in res]
    return res


# Time: O(n * 2^n)
# Space: O(2^n)
# It's a backtracking problem, which can be solved by iterating over all elements and adding each one into the result set, then recursively expand the result set.
# Here are some key points to understand the code:
# 1. The result is built by adding each element from the original list into the result set. This is why the res += [j + [i] for j in res] line is used. It generates all the combinations of each element in the result set with all the elements in the original list.
# 2. The time complexity is O(n * 2^n) because we need to iterate over the original list and the result set, and the result set has 2^n elements.
# 3. The space complexity is O(2^n) because the result set can have up to 2^n elements.
# 4. The code can be optimized by limiting the length of the generated combinations, but it's not necessary if you only need to generate all the combinations.
# 5. This solution can be extended to generate all the combinations of multiple lists.
# Here are some key points to understand the code:
# 1. The result is built by adding each element from the original list into the result set. This is why the res += [j + [i] for j in res] line is used. It generates all the combinations of each element in the result set with all the elements in the original list.
# 2. The time complexity is O(n * 2^n) because we need to iterate over the original list and the result set, and the result set has 2^n elements.
# 3. The space complexity is O(2^n) because the result set can have up to 2^n elements.
# 4. The code can be optimized by limiting the length of the generated combinations, but it's not necessary