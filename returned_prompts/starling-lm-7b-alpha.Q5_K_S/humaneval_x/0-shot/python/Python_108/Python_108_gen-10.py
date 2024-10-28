
def count_nums(arr):
    return sum(map(sum, arr))


# Alternative solution
def count_nums(arr):
    return sum(map(lambda x: sum(map(int, str(x))), arr))


# Testing
print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)


# Testing the alternative solution
print(sum(map(sum, [1, 1, 2])))
print(map(lambda x: sum(map(int, str(x))), [1, 1, 2]))


# Alternative solution - Using reduce
from functools import reduce

def count_nums(arr):
    return reduce(lambda x,y: x+y, map(lambda x: sum(map(int, str(x))), arr))


# Testing the alternative solution
print(reduce(lambda x,y: x+y, map(lambda x: sum(map(int, str(x))), [1, 1, 2])))


# Alternative solution - Using itertools.chain
from itertools import chain

def count_nums(arr):
    return sum(map(int, chain(*map(str, arr))))


# Testing the alternative solution
print(sum(map(int, chain(*map(str, [1, 1, 2])))))


# Alternative solution - Using itertools.starmap
from itertools import starmap

def count_nums(arr):
    return sum(starmap(int, map(str, arr)))


# Testing the alternative solution
print(sum(starmap(int, map(str, [1, 1, 2]))))


# Alternative solution - Using itertools.accumulate
from itertools import accumulate

def count_nums(arr):
    return len(accumulate(map(sum, map(int, map(str, arr)))))


# Testing the