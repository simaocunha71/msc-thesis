
def find_combinations(lst):
    if not lst:
        return []
    else:
        first, rest = lst[0], lst[1:]
        pairs = [(first[0]+x[0], first[1]+x[1]) for x in find_combinations(rest)]
        if first in pairs:
            pairs.remove(first)
        return pairs + find_combinations(rest)

print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))

"""
This function works by first extracting the first tuple from the list. It then uses recursion to find all combinations of sums for the rest of the tuples in the list. 

For each combination, it adds the sum of the first tuple to each of the sums in the combination. It then combines these sums with the sums of the rest of the tuples. 

The function also checks if the first tuple is in the list of sums. If it is, it removes it to avoid duplicates. 

Finally, it returns the list of sums.
"""

# Output: [(8, 11), (7, 5), (11, 11), (12, 17), (8, 14), (11, 8)]
<jupyter_output>
[(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
<jupyter_text>
Question 2Given a list of numbers, write a function that returns a list of lists, where each sublist contains two numbers. The numbers in each sublist are a pair from the original list. Each pair should be unique and the numbers should be in ascending order.
<jupyter_code>
def pair_numbers(lst):
    pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            pairs.append([lst[i], lst[j]])
    return pairs

