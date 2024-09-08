
def extract_singly(lst):
    flat_list = []
    for sublist in lst:
        for item in sublist:
            flat_list.append(item)
    return flat_list

assert set(extract_singly([(3, 4, 5),  (4, 5, 7),  (1, 4)])) == set([3, 4, 5, 7, 1])

"""
Write a function that takes two lists of integers and returns True if they have at least one common member.
"""

def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if len(a_set.intersection(b_set)) > 0: 
        return True
    return False

print(common_member([1,2,3,4], [3,4,5,6])) # should return True
print(common_member([1,2,3,4], [5,6,7,8])) # should return False
<jupyter_output>
True
False
<jupyter_text>
Exercise 3: String manipulation
<jupyter_code>
"""
Write a function that takes a string and returns a string where all the characters are reversed.
"""

def reverse_string(s):
    return s[::-1]

print(reverse_string("Hello, World!")) # should return "dlroW ,olleH"

"""
Write a function that takes a string and returns a string where all the words are reversed.
"""

def reverse_words(s):
    return ' '.join(s.split()[::-1])

print(reverse_words("Hello, World!")) # should return "World dlroW ,Hello"

"""
Write a function that takes a string and returns a string where all the words are reversed but the letters in each word are not.
"""

def reverse_words_letters(s):
    return ' '.join(word[::-1] for word in s.split())

print(reverse_words_letters("