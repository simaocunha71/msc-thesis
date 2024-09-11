def unique_Element(nums):
    # Convert the list to a set to remove duplicates.
    # If the length of the set is equal to the length of the original list, then all elements are unique.
    return len(set(nums)) == len(nums)

# Test the function
assert unique_Element([1,1,1]) == True
assert unique_Element([1,2,3]) == False

# Extra
# To solve this problem, you can also use the Counter class from the collections module, which counts the number of occurrences of each element in an iterable.

from collections import Counter
def unique_Element2(nums):
    return len(Counter(nums)) == 1

assert unique_Element2([1,1,1]) == True
assert unique_Element2([1,2,3]) == False

# Extra
# To solve this problem, you can also use the any function. The any function returns True if at least one element of the iterable is True. Otherwise, it returns False.

def unique_Element3(nums):
    return any(nums.count(i) == 1 for i in nums)

assert unique_Element3([1,1,1]) == True
assert unique_Element3([1,2,3]) == False

# Extra
# To solve this problem, you can also use the reduce function from the functools module, which applies a function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single output.

from functools import reduce
def unique_Element4(nums):
    return reduce(lambda x,y: x and y, (nums.count(i) == 1 for i in nums))

assert unique_Element4([1,1,1]) == True
assert unique_Element4([1,2,3]) == False

# Extra
# To solve this problem, you can also use the all function. The all function returns True if all elements of the iterable are true. Otherwise, it returns False.

def unique_Element5(nums):
    return all(nums.count(i) == 1 for i in