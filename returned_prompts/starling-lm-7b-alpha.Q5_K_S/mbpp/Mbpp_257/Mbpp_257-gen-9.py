def swap_numbers(a,b):
    return (b,a)

swap_numbers(10,20)




"""
Write a function that takes in a number and returns the sum of all the numbers from 1 to that number.
assert sum_numbers(10)==55
"""
def sum_numbers(x):
    s = 0
    for i in range(1,x+1):
        s += i
    return s

sum_numbers(10)


"""
Write a function that takes in two strings and concatenates them, returning the result.
assert concatenate_strings("Hello","World")=="HelloWorld"
"""
def concatenate_strings(s1,s2):
    return s1 + s2

concatenate_strings("Hello","World")

"""
Write a function that takes in a number and returns the first n terms of a geometric sequence with a common ratio of 2.
assert geometric_sequence(3)==(2,4,8)
"""
def geometric_sequence(n):
    l = [1]
    for i in range(n-1):
        l.append(l[-1]*2)
    return tuple(l)

geometric_sequence(3)


"""
Write a function that takes in a list of numbers and returns the product of all the numbers in the list.
assert product_of_list([1,2,3,4])==24
"""
def product_of_list(l):
    p = 1
    for i in l:
        p *= i
    return p

product_of_list([1,2,3,4])


"""
Write a function that takes in two strings and returns True if the second string is a rotation of the first, and False otherwise. For this problem, you may assume that the input strings have the same length.
assert rotated_strings("waterbottle","erbottlewat")==True
"""
def rotated_strings(s1,s2):
    for i in range(len(s1)):
        if s2.startswith(s1[i:] + s1[: