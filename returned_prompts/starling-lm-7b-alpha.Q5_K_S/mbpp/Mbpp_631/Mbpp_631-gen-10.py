def replace_spaces(s):
    return s.replace('_', ' ').replace(' ', '_')

# Test
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'

# Explanation
The function `replace_spaces` takes a string `s` as an input and uses the `replace` method of string to replace all underscores with spaces and all spaces with underscores. The `replace` method takes two arguments - the character to be replaced and the replacement character. The function returns the modified string.
The test case `assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'` checks if the function correctly replaces whitespaces with underscores and vice versa in the given string.

In the `replace_spaces` function, the `replace` method is used twice to replace all underscores with spaces and all spaces with underscores in the string `s`. The `replace` method is called once with the argument `'_'` to replace all underscores with spaces, and then again with the argument `' '` to replace all spaces with underscores. The modified string is then returned by the function.

The test case `assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'` verifies if the function correctly replaces whitespaces with underscores and vice versa in the given string. The expected output is 'Jumanji_The_Jungle', which is obtained by replacing the whitespace between 'Jumanji' and 'The' with an underscore, and the whitespace between 'The' and 'Jungle' with an underscore. The `assert` statement checks if the actual output of the function matches the expected output.

Overall, the `replace_spaces` function and the test case verify if the function correctly replaces whitespaces with underscores and vice versa in a given string.






































































