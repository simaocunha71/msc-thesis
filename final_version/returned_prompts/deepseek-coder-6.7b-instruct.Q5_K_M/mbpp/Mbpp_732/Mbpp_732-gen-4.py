def replace_specialchar(s):
    special_char = [' ', ',', '.']
    for char in special_char:
        s = s.replace(char, ':')
    return s

s = 'Python language, Programming language.'
print(replace_specialchar(s))
<jupyter_output>
Python:language::Programming:language:
<jupyter_text>
Q2. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, and 18.
<jupyter_code>
def sum_multiples(limit):
    result = 0
    for i in range(1, limit+1):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

print(sum_multiples(20))
<jupyter_output>
98
<jupyter_text>
Q3. Write a function that prints all the unique combinations of [1, 2, 3] and [3, 2, 1] using the itertools library in Python.
<jupyter_code>
import itertools

def unique_combinations():
    list1 = [1, 2, 3]
    list2 = [3, 2, 1]

    combined_list = list(itertools.product(list1, list2))
    return combined_list

print(unique_combinations())
<jupyter_output>
[(1, 3), (1, 2), (1, 1), (2, 3), (2, 2), (2, 1), (3, 3), (3, 2), (3, 1)]
<jupyter_text>
Q4. Write a function that takes a string and returns a dictionary with the count of each character in the string as values.
<jupyter_code>
def char_count(s):
    count_dict