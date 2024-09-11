def replace_specialchar(s):
    return s.replace(" ", ":").replace(",", ":").replace(".", ":")

# assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
# print(replace_specialchar('Python language, Programming language.'))







"""
Given a list of strings, return a list of strings where the first and last letters of each string are swapped.

For example, if you are given the list ["apple", "banana"], you should return ["leppa", "ananab"].

Here are some more test cases to ensure that your code is working correctly:

assert swap_first_last(["cat", "dog", "mouse"]) == ["atoc", "god", "semou"]
assert swap_first_last(["Python", "programming"]) == ["noyhtP", "gnimmargorp"]

You can use Python's slicing feature to solve this problem. Here's how you can use it:

To swap the first and last letters of a string, you can use the syntax string[0] and string[-1].
To create a new string with the first and last letters swapped, you can use string[1:-1].join(string[0], string[-1])
To create a list of strings with the first and last letters swapped for each string, you can use map(swap_first_last, list_of_strings)
"""

def swap_first_last(list_of_strings):
    return list(map(lambda string:string[1:-1].join(string[0], string[-1]), list_of_strings))

# assert swap_first_last(["cat", "dog", "mouse"]) == ["atoc", "god", "semou"]
# assert swap_first_last(["Python", "programming"]) == ["noyhtP", "gnimmargorp"]
# print(swap_first_last(["Python", "programming"]))

"""
In this problem, you will need to write a function that takes two parameters, a string and a number, and returns the string repeated the number of times specified by the number parameter.
