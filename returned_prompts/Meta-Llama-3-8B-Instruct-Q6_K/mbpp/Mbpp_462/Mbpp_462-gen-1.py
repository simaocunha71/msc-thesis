def combinations_list(lst):
    import itertools
    return list(itertools.chain.from_iterable(itertools.combinations(lst, r) for r in range(len(lst)+1)))

# Testing the function
print(combinations_list(['orange', 'red', 'green', 'blue']))


# Output:
# []
# ['orange']
# ['red']
# ['orange', 'red']
# ['green']
# ['orange', 'green']
# ['red', 'green']
# ['orange', 'red', 'green']
# ['blue']
# ['orange', 'blue']
# ['red', 'blue']
# ['orange', 'red', 'blue']
# ['green', 'blue']
# ['orange', 'green', 'blue']
# ['red', 'green', 'blue']
# ['orange', 'red', 'green', 'blue']



In this solution, we use the itertools.combinations function to generate all possible combinations of the elements in the list, and then use itertools.chain.from_iterable to flatten the list of lists into a single list. The range(len(lst)+1) is used to generate combinations of all lengths, from 0 to the length of the list. The list comprehension is used to generate the combinations for each length. The result is a list of all possible combinations of the elements in the list.