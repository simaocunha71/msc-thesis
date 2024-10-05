
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    s = s.split()
    res = []
    for i in s:
        res.append(''.join(sorted(i)))
    return ' '.join(res)

# Testing
print(anti_shuffle('Hi'))
print(anti_shuffle('hello'))
print(anti_shuffle('Hello World!!!'))




# Code Explanation
# The function anti_shuffle(s) takes a string and splits it into a list of words using the split() method.
# Then, a new empty list called res is created to store the ordered versions of the words.
# A for loop is used to iterate over each word in the s list.
# For each word, the sort() method is used to arrange the characters in ascending order based on their ASCII values.
# The sorted characters are then joined back together using the join() method, and the result is appended to the res list.
# Finally, the join() method is used again to concatenate all the ordered words in the res list, separated by a space, and the result is returned.

# Testing the function with the provided examples:
# anti_shuffle('Hi') returns 'Hi'
# anti_shuffle('hello') returns 'ehllo'
# anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'





















































