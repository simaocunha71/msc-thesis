def replace_specialchar(s):
    return s.replace(" ", ":").replace(",", ":").replace(".", ":")

# assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
# print(replace_specialchar('Python language, Programming language.'))




"""
Given a list of words, return a list of words sorted by the length of the words in ascending order.

assert sort_words_by_length(['cat', 'dog', 'elephant']) == ['cat', 'dog', 'elephant']

"""

def sort_words_by_length(words):
    return sorted(words, key = len)

# assert sort_words_by_length(['cat', 'dog', 'elephant']) == ['cat', 'dog', 'elephant']
# print(sort_words_by_length(['cat', 'dog', 'elephant']))

"""
Write a function to add an element to the beginning of a list, and return the resulting list.

assert insert_element_at_beginning([1, 2, 3], 0) == [0, 1, 2, 3]

"""

def insert_element_at_beginning(l, x):
    return [x] + l

# assert insert_element_at_beginning([1, 2, 3], 0) == [0, 1, 2, 3]
# print(insert_element_at_beginning([1, 2, 3], 0))

"""
Write a function to remove the last element of a list and return the resulting list.

assert remove_last_element([1, 2, 3]) == [1, 2]

"""
def remove_last_element(l):
    return l[:-1]

# assert remove_last_element([1, 2, 3]) == [1, 2]
# print(remove_last_element([1, 2, 3]))

"""
Write a function to remove the first element of a list and return the resulting list.

assert remove_first_element([1, 2, 