def number_of_substrings(s):
    return sum(len(s[i:]) for i in range(len(s)))

print(number_ofof_substrings("abc"))  # Output: 6

Explanation:
The function `number_of_substrings` takes a string `s` as input.
It calculates the sum of the lengths of all non-empty substrings of the string.
For each character in the string, it calculates the length of all substrings starting from that character (including the string starting from that character).
This gives the number of non-empty substrings starting from that character.
The `range(len(s))` generates the indices of the characters in the string, and `s[i:]` generates the substrings starting from that character.
The `len(s[i:])` gives the length of the substring starting from the `i`th character.
The `sum` function adds up these lengths to give the total number of non-empty substrings.
"""

