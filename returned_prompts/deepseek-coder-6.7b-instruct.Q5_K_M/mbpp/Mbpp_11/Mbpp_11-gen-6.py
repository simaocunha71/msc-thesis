
def remove_Occ(s, c):
    # find the first and last occurrence of the character
    first_occurrence = s.find(c)
    last_occurrence = s.rfind(c)

    # remove the first and last occurrence
    if first_occurrence != -1 and last_occurrence != -1:
        s = s[:first_occurrence] + s[last_occurrence + 1:]
    return s

print(remove_Occ("hello", "l"))  # returns: "heo"


# Explanation:
# The function `remove_Occ` takes a string `s` and a character `c` as inputs and finds the first and last occurrence of the character in the string.
# If the character exists in the string, it removes the first occurrence and the last occurrence from the string.
# The modified string is then returned. If the character does not exist in the string, the original string is returned.
# The `find` method returns the index of the first occurrence of the character in the string, and the `rfind` method returns the index of the last occurrence of the character in the string.
# The slicing operation `s[:first_occurrence] + s[last_occurrence + 1:]` removes the first occurrence and the last occurrence from the string.
<jupyter_output>
heo
<jupyter_text>
4. Write a Python Program to count the number of vowels in a string.
<jupyter_code>
# Python program to count the number of vowels in a string

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

string = "Hello World"
print(f"Number of vowels in string {string} is : {count_vowels(string)}")
<jupyter_output>
Number of vowels in string Hello World is : 3
<jupyter_text>
5. Write a Python Program to count the number of consonants in a string.
<jupyter