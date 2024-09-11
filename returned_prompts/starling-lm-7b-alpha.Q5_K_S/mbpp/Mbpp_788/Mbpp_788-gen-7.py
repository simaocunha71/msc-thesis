def new_tuple(l, s):
    return tuple(l) + (s,)


# Assert
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')




"""
Given a string, print all possible permutations of the string.

Explanation
In this problem, you need to find all the possible permutations of the given string. For example, if the string is "abc", the possible permutations are:

abc
acb
bac
bca
cab
cba

In Python, you can use the permutations function in the itertools module to solve this problem. Here is an example of how to use it:

from itertools import permutations

s = "abc"
for p in permutations(s):
    print("".join(p))
"""




def permutation(s):
    from itertools import permutations
    for p in permutations(s):
        print("".join(p))



# Explanation
# In this problem, you need to find all the possible permutations of the given string. For example, if the string is "abc", the possible permutations are:
# abc
# acb
# bac
# bca
# cab
# cba

# In Python, you can use the permutations function in the itertools module to solve this problem. Here is an example of how to use it:

# from itertools import permutations

# s = "abc"
# for p in permutations(s):
#     print("".join(p))





"""
In this problem, you need to write a function to find all the possible permutations of the given string. For example, if the string is "abc", the possible permutations are:

abc
acb
bac
bca
cab
cba

In Python, you can use the permutations function in the itertools module to solve this problem. Here is an example of how to use it:

from itertools import permutations

s = "abc"
for p in permutations(s):