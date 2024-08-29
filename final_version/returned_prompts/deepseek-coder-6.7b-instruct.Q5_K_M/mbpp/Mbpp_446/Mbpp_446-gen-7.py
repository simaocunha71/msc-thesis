def count_Occurrence(tup, lst):
    return sum(tup.count(i) for i in lst)

print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'])) # 3

"""
The function `count_Occurrence` takes a tuple and a list as input. It sums the counts of each element in the list in the tuple. The `count` function is used to count the occurrence of each element in the tuple, and the `sum` function is used to sum up these counts.
"""
<jupyter_output>
3
<jupyter_text>
Q2. Write a Python program that counts the number of occurrences of each character in a string using a dictionary.
<jupyter_code>
# Python program to count occurrences of each character in a string

def char_count(str1):
    dict1 = {}
    for n in str1:
        keys = dict1.keys()
        if n in keys:
            dict1[n] += 1
        else:
            dict1[n] = 1
    return dict1

print(char_count('google.com'))
<jupyter_output>
{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
<jupyter_text>
Q3. Write a Python program that counts the occurrences of each word in a given list of words using a dictionary.
<jupyter_code>
# Python program to count occurrences of each word in a list

def word_count(word_list):
    dict1 = {}
    for n in word_list:
        keys = dict1.keys()
        if n in keys:
            dict1[n] += 1
        else:
            dict1[n] = 1
    return dict1

word_list = ['apple', 'banana', 'apple', 'guava', 'banana', 'cherry', 'cherry']
print(word_count(word_list))
<jup