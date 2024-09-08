def find_Max_Num(lst):
    lst.sort(reverse=True)
    return int("".join(map(str, lst)))

print(find_Max_Num([1,2,3])) #321


# Other way to solve the problem
def find_Max_Num_v2(lst):
    lst = [str(i) for i in lst]
    lst.sort(reverse=True)
    return int("".join(lst))

print(find_Max_Num_v2([1,2,3])) #321


# Using Python's built-in function `functools.cmp_to_key`
from functools import cmp_to_key

def find_Max_Num_v3(lst):
    lst = [str(i) for i in lst]
    lst.sort(key=cmp_to_key(lambda a, b: int(b+a) - int(a+b)), reverse=True)
    return int("".join(lst))

print(find_Max_Num_v3([1,2,3])) #321


# Using Python's built-in function `operator.itemgetter`
from operator import itemgetter

def find_Max_Num_v4(lst):
    lst = [str(i) for i in lst]
    lst.sort(key=itemgetter(0), reverse=True)
    return int("".join(lst))

print(find_Max_Num_v4([1,2,3])) #321


# Using Python's built-in function `itertools.permutations`
from itertools import permutations

def find_Max_Num_v5(lst):
    return max(int("".join(p)) for p in permutations(map(str, lst)))

print(find_Max_Num_v5([1,2,3])) #321


# Using Python's built-in function `max`
def find_Max_Num_v6(lst):
