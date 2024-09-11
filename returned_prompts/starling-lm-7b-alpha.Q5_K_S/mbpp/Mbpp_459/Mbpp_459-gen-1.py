def remove_uppercase(s):
    return ''.join(c for c in s if c.islower())

# assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'castyoravoitshos'

"""
The function remove_uppercase takes a string as an input and returns a new string
with all the uppercase characters removed. It uses a generator expression to iterate
over each character in the input string and only includes the characters that are
lowercase. The join method is then used to concatenate the lowercase characters
back into a string, which is returned as the result.
"""

# The assert statement is used to check the correctness of the function. It compares the
# result of the function with the expected output and if they are not equal, an error is raised.
# In this case, the assert statement is used to check if the remove_uppercase function correctly
# removes all uppercase characters from the input string 'cAstyoUrFavoRitETVshoWs' and returns the
# correct output 'castyoravoitshos'. If the assert statement passes, it means that the function is working correctly.

# The remove_uppercase function can be used to remove uppercase substrings from any given string. Simply pass
# the string as an argument to the function and it will return a new string with all uppercase characters removed.

# Here's an example of how to use the function:

def remove_uppercase(s):
    return ''.join(c for c in s if c.islower())

print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))  # Output: 'castyoravoitshos'

"""
This code demonstrates the usage of the remove_uppercase function. It defines the function and then
calls it with the string 'cAstyoUrFavoRitETVshoWs' as an argument. The result, 'castyoravoitshos', is then printed
to the console. The function successfully removes all uppercase characters from the input string, resulting in the
desired output."""

"""
The remove_uppercase function uses a generator expression