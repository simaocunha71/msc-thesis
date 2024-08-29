def remove_uppercase(s):
    return "".join([i for i in s if not i.isupper()])

print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))
<jupyter_output>
cstyoravoitshos
<jupyter_text>
1.4.5 Practice Problems: String Operations  Problem 1: Count Lowercase Letters in a StringWrite a function that counts the number of lowercase letters in a string. The function should return a dictionary with keys as lowercase letters and values as their counts.
<jupyter_code>
def count_lowercase_letters(s):
    # Your code here
    pass

# Test
s = "Hello World"
print(count_lowercase_letters(s))  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2: Remove Uppercase LettersWrite a function that removes all the uppercase letters from a given string.
<jupyter_code>
def remove_uppercase(s):
    # Your code here
    pass

# Test
s = "Hello World"
print(remove_uppercase(s))  # Output: 'ello Worl'
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3: Count WordsWrite a function that counts the number of words in a string. The function should return a dictionary with keys as words and values as their counts.
<jupyter_code>
def count_words(s):
    # Your code here
    pass

# Test
s = "Hello Hello World"
print(count_words(s))  # Output: {'hello': 2, 'world': 1}
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 4: Capitalize WordsWrite a