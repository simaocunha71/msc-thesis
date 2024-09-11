def remove_Occ(s, c):
    return s[s.index(c)+1:len(s)-s[::-1].index(c)]

# Python3 program to print prime factors
# of a given number

# Function to remove first and
# last occurrence of c from s
def remove_Occ(s, c):
    # find the index of c
    # in the given string
    i = s.index(c)

    # find the index of c in reverse
    # order of the given string
    j = s[::-1].index(c)

    # check if the first and last
    # occurrence of c is present
    if i == 0 and j == len(s)-1:
        return s

    # return the string after removing
    # first and last occurrence of c
    return s[i+1:len(s)-j]


# Driver code

"""
Explanation

The function remove_Occ takes two parameters: a string s and a character c. It uses two methods to find the index of c in the string s. The first method, s.index(c), finds the index of the first occurrence of c in the string. The second method, s[::-1].index(c), finds the index of the last occurrence of c in the string, but in reverse order.

The function then checks if the first and last occurrence of c are at the beginning and end of the string, respectively. If they are, it returns the original string. Otherwise, it returns a new string that is s without the first and last occurrence of c.

In the provided example, the function remove_Occ("hello","l") is called, which will return "heo" because the first and last occurrence of "l" in "hello" are removed.

"""

# Python3 program to print prime factors
# of a given number

# Function to remove first and
# last occurrence of c from s
def remove_Occ(s, c):
    # find the index of c
    # in the given string
    i = s.index(c)

    # find the index of c in reverse
    # order of the given string
    j = s[