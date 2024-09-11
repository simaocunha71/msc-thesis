def find_substring(string_list,sub_str):
    for i in string_list:
        if sub_str in i:
            return True
    return False

"""
Write a function to get the length of a string
"""
def get_length(s):
    return len(s)

"""
Write a function to get the first element of a list
"""
def get_first(lst):
    return lst[0]

"""
Write a function to get the last element of a list
"""
def get_last(lst):
    return lst[-1]

"""
Write a function to get the second element of a list
"""
def get_second(lst):
    return lst[1]


"""
Write a function to get the third element of a list
"""
def get_third(lst):
    return lst[2]

"""
Write a function to get the nth element of a list
"""
def get_nth(lst,n):
    return lst[n-1]

"""
Write a function to get the minimum element of a list
"""
def get_min(lst):
    return min(lst)

"""
Write a function to get the maximum element of a list
"""
def get_max(lst):
    return max(lst)

"""
Write a function to check if a number is even
"""
def is_even(num):
    return num%2==0

"""
Write a function to check if a number is odd
"""
def is_odd(num):
    return num%2!=0

"""
Write a function to check if a number is prime
"""
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

"""
Write a function to get the sum of all the elements in a list
"""
def sum_list(lst):
    return sum(lst)

"""
Write a function to get the average of all the elements in a list
"""
def average(lst):
    return sum(lst)/len(lst