
def remove_all_spaces(string):
    return string.replace(' ', '')

print(remove_all_spaces('python  program'))

"""
The function remove_all_spaces uses the replace() method of the string object, which replaces all occurrences of a specified character with another character. In this case, it replaces all whitespace characters (' ') with no character (''), effectively removing them.
"""
<jupyter_output>
pythonprogram
<jupyter_text>
Question 2: Write a function to return the count of characters in a string.
<jupyter_code>
def count_characters(string):
    count = 0
    for char in string:
        count += 1
    return count

print(count_characters('hello'))
<jupyter_output>
5
<jupyter_text>
Question 3: Write a function to return the count of vowels in a string.
<jupyter_code>
def count_vowels(string):
    count = 0
    vowels = 'aeiouAEIOU'
    for char in string:
        if char in vowels:
            count += 1
    return count

print(count_vowels('hello'))
<jupyter_output>
2
<jupyter_text>
Question 4: Write a function to return the count of consonants in a string.
<jupyter_code>
def count_consonants(string):
    count = 0
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    for char in string:
        if char in consonants:
            count += 1
    return count

print(count_consonants('hello'))
<jupyter_output>
3
<jupyter_text>
Question 5: Write a function to return the count of digits in a string.
<jupyter_code>
def count_digits(string):
    count = 0
    digits = '01234