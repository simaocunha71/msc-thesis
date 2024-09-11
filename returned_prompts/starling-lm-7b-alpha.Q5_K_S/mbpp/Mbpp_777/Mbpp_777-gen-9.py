def find_sum(lst):
    seen = set()
    total = 0
    for item in lst:
        if item not in seen:
            total += item
            seen.add(item)
    return total


# Test the function
assert find_sum([1,2,3,1,1,4,5,6]) == 21

# More tests
assert find_sum([1,2,3,4]) == 10
assert find_sum([1,1,2,3,3]) == 7



def find_sum_v2(lst):
    return sum(lst) - len(lst) * min(lst)


# Test the function
assert find_sum_v2([1,2,3,1,1,4,5,6]) == 21
assert find_sum_v2([1,2,3,4]) == 10
assert find_sum_v2([1,1,2,3,3]) == 7


def find_sum_v3(lst):
    return sum(set(lst))


# Test the function
assert find_sum_v3([1,2,3,1,1,4,5,6]) == 21
assert find_sum_v3([1,2,3,4]) == 10
assert find_sum_v3([1,1,2,3,3]) == 7


def find_sum_v4(lst):
    return sum(set(lst)) - len(set(lst)) * min(set(lst))


# Test the function
assert find_sum_v4([1,2,3,1,1,4,5,6]) == 21
assert find_sum_v4([1,2,3,4]) == 10
assert find_sum_v4([1,1,2,3,3]) == 7


"""
In the above code, we have implemented the function find_sum to find the sum of non-repeated elements in a given list.
We have implemented four different versions of this function:

1. find_sum: This version uses a set to keep