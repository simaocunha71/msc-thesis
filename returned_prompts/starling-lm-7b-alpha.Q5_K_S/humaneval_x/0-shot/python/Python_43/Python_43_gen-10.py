    # if len of list is even, then return False
    if len(l) % 2 == 0:
        return False
    # if len of list is odd, then create a set from the list
    else:
        l = set(l)
        # for each num in list, then check if (-num) is in the set
        for num in l:
            if -num in l:
                return True
        return False






# Created by: Madelyn
# Date: Dec 18, 2020
# This program takes a list of integers as an input and returns True if there are two
# distinct elements in the list that sum to zero, and False otherwise.

# The program starts by checking if the length of the list is even. If the length
# is even, this means that there are an even number of elements in the list. Since
# each pair of elements has to be a sum of two distinct elements, there can't be
# an even number of elements that sum to zero. Therefore, if the length of the
# list is even, the program immediately returns False.

# If the length of the list is odd, then the program creates a set from the list.
# This is because sets only contain unique elements, so if we create a set from
# the list, any duplicate elements will be removed. The program then checks if
# the negation of each number in the set is in the set. If the negation of a
# number is in the set, this means that there are two distinct elements in the
# list that sum to zero. Therefore, if the negation of any number is in the set,
# the program returns True.

# If the program goes through all the numbers in the set without finding any
# that have a negation in the set, this means that there are no two distinct
# elements in the list that sum to zero. Therefore, the program returns False.



# Here are some example test cases for the program:

# When the program is given the list [1, 3, 5, 0], it should return False.
# This is because there are no two distinct elements in the list that sum to zero.
# The program correctly returns False.

# When the