"""
This problem can be solved by using itertools.product() to generate all possible combinations of sums with tuples in the given tuple list.

Here is the Python code for the problem:
"""
import itertools

def find_combinations(lst):
    combs = list(itertools.product(*lst))
    return [(sum(x), sum(y)) for x, y in combs]

assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]

"""
This code first uses itertools.product() to generate all possible combinations of tuples in lst. It then sums the elements in each tuple and returns a list of tuples.
"""

"""
Note: The time complexity of this solution is O(n^2), where n is the length of the input list. This is because itertools.product() generates all possible combinations of the input lists, and for each combination, it sums the elements of the tuples.
"""

"""
Another way to solve this problem is to use recursion. Here is the Python code for the problem:
"""

def find_combinations(lst):
    def helper(lst, idx, path, res):
        if idx == len(lst):
            res.append((sum(path[0]), sum(path[1])))
            return
        for i in range(len(lst[idx])):
            path[idx].append(lst[idx][i])
            helper(lst, idx + 1, path, res)
            path[idx].pop()
    res = []
    path = [[] for _ in range(len(lst))]
    helper(lst, 0, path, res)
    return res

assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5