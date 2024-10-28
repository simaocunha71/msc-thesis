    def order_by_points(nums):
        nums = [(i, sum(map(int, str(i))), index) for index, i in enumerate(nums)]
        return sorted(nums, key=lambda x: (x[1], x[2]))

    return order_by_points(nums)




# Python3 program to find
# all subsets with sum equal
# to given sum

from itertools import combinations

def find_subsets(nums, target_sum):
    result = []
    for i in range(len(nums)+1):
        for subset in combinations(nums, i):
            if sum(subset) == target_sum:
                result.append(subset)
    return result




# Python3 program to find all
# permutations of a string

from itertools import permutations

def find_permutations(s):
    result = []
    for perm in permutations(s):
        result.append(''.join(perm))
    return result




# Python3 program to find all
# permutations of a list

def find_permutations(nums):
    result = []
    for perm in permutations(nums):
        result.append(list(perm))
    return result




# Python3 program to print all
# subsets of a given set

from itertools import chain, combinations

def print_subsets(nums):
    for i in range(len(nums)+1):
        for subset in combinations(nums, i):
            print(list(subset))
    return None




# Python3 program to find all
# permutations of a string

from itertools import permutations

def find_permutations(s):
    result = []
    for perm in permutations(s):
        result.append(''.join(perm))
    return result




# Python3 program to find all
# permutations of a list

from itertools import permutations

def find_permutations(nums):
    result = []
   