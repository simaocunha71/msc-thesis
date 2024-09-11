def snake_to_camel(snake_case):
    camel_case = ""
    for i in range(len(snake_case)):
        if(i == 0):
            camel_case += snake_case[i].upper()
        else:
            if(snake_case[i] == "_"):
                camel_case += snake_case[i+1].upper()
            else:
                camel_case += snake_case[i]
    return camel_case

# Test the function
assert snake_to_camel('python_program')=='PythonProgram'
print("Tests Passed")

# Extra Test
assert snake_to_camel('python_program_test')=='PythonProgramTest'
print("Tests Passed")


"""
Explanation:
The function snake_to_camel takes a string in snake case as an argument and converts it to camel case.
In a snake case string, the words are separated by underscores (_).
In a camel case string, the first letter of each word is capitalized.
The function iterates through each character in the snake case string.
For the first character, it capitalizes it and adds it to the camel case string.
For each subsequent character, if the character is an underscore (_), it capitalizes the next character and adds it to the camel case string.
If the character is not an underscore, it adds the character as is to the camel case string.
Finally, the function returns the camel case string.
"""

"""
Explanation:
The function snake_to_camel takes a string in snake case as an argument and converts it to camel case.
In a snake case string, the words are separated by underscores (_).
In a camel case string, the first letter of each word is capitalized.
The function iterates through each character in the snake case string.
For the first character, it capitalizes it and adds it to the camel case string.
For each subsequent character, if the character is an underscore (_), it capitalizes the next character and adds it to the camel case string.
If the character is not an underscore, it adds the character as is to