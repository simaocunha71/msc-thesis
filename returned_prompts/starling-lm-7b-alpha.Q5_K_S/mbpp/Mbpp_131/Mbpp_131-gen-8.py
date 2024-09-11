def reverse_vowels(s):
    s = list(s)
    vowels = "aeiou"
    left, right = 0, len(s) - 1
    while left < right:
        while s[left] not in vowels:
            left += 1
        while s[right] not in vowels:
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

assert reverse_vowels("Python") == "Python"

# Python3 program to print all possible
# permutations of a string

'''
In this code, we are finding the
permutations of the string in the lexicographical
order. The time complexity of this function
is O(n*n!) '''

from itertools import permutations

def string_permutations(str):
    # This function prints all the permutations
    # of the string str. 
    perms = set(permutations(str))
    # Convert the set to a list and print the elements
    # of the list. Each element of the list is a tuple
    # containing all the permutations of the string
    return list(perms)

def string_permutations_lexicographical(str):
    return list(permutations(str))

def string_permutations_lexicographical_inplace(str):
    p = string_permutations(str)
    p.sort()
    return p

def string_permutations_lexicographical_inplace_using_itertools(str):
    p = list(permutations(str))
    p.sort()
    return p

def string_permutations_lexicographical_inplace_using_sorted(str):
    p = list(permutations(str))
    p.sort()
    return p

def string_permutations_lexicographical_inplace_using_sorted_list(str):
    p = list(permutations(str))
    p.sort()
    return p

