def combinations_colors(lst, length):
    result = []
    for i in range(length):
        result.append(tuple(lst[i] for i in range(length)))
    return result





"""
Write a function that takes in a list of integers and a number n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.

The function should use a generator function to create a generator object that yields tuples of elements.

The function should have a time complexity of O(N) where N is the length of the input list.
"""

def combinations(nums, length):
    def generate_combinations(i, curr_comb, result):
        if i == length:
            result.append(tuple(curr_comb))
        else:
            for j in range(i, length):
                curr_comb[i] = nums[j]
                generate_combinations(i+1, curr_comb, result)

    curr_comb = [None]*length
    generate_combinations(0, curr_comb, [])
    return result


"""
Write a function that takes in a list and length n, and generates all permutations (with repetition) of the elements of the list and returns a list with a tuple for each permutation.

The function should use a generator function to create a generator object that yields tuples of elements.

The function should have a time complexity of O(N!) where N is the length of the input list.
"""

def permutations(nums, length):
    def generate_permutations(i, curr_perm, result):
        if i == length:
            result.append(tuple(curr_perm))
        else:
            for j in range(i, length):
                curr_perm[i] = nums[j]
                generate_permutations(i+1, curr_perm, result)

    curr_perm = [None]*length
    generate_permutations(0, curr_perm, [])
    return result




"""
Write a function that takes in a list of integers and a number