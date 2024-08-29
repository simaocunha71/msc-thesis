def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

print(second_smallest([1, 2, -8, -2, 0, -2]))

#This program will find the second smallest number in a list. The function works by initializing two variables m1 and m2 with infinity. Then it iterates through the list. If it encounters a number that is smaller than or equal to m1, it updates m1 and m2 with the new number and the old m1. If it encounters a number that is between m1 and m2, it updates m2 with the new number. The result is the second smallest number in the list.
<jupyter_output>
-2
<jupyter_text>
2. Write a Python program to reverse a string. Sample String : "1234abcd" Expected Output : "dcba4321"
<jupyter_code>
def reverse_string(s):
    return s[::-1]

print(reverse_string("1234abcd"))
<jupyter_output>
dcba4321
<jupyter_text>
3. Write a Python program to split and join a string.
<jupyter_code>
def split_and_join(line):
    # split the line into words
    words = line.split(" ")
    
    # join the words with a hyphen
    return "-".join(words)

print(split_and_join("This is a string to split and join"))
<jupyter_output>
This-is-a-string-to-split-and-join
<jupyter_text>
4. Write a Python program to check if a given key already exists in a dictionary.
<jupyter_code>
def key_exists(dict, key):
    return key in dict

my_dict = {'a': 1, 'b': 2