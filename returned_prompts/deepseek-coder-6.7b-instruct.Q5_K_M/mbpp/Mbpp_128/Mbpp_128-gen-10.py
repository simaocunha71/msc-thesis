def long_words(n,words):
    result = [word for word in words.split() if len(word) > n]
    return result

print(long_words(3,"python is a programming language"))

# Output: ['python', 'programming', 'language']

# Solution Explanation:
# The function 'long_words' takes two parameters 'n' and 'words'. 'n' is the minimum length of words we want to include, and 'words' is the string of words.
# We use the split() method to divide the string into a list of words.
# The list comprehension [word for word in words.split() if len(word) > n] generates a list of words that are longer than 'n' characters.
# Finally, the function returns this list.
<jupyter_output>
['python', 'programming', 'language']
<jupyter_text>
Q2. Write a Python function to count the number of words that start and end with the same letter in a given list of words.
<jupyter_code>
# Python Solution:

def count_words(words):
    return sum(1 for word in words if word[0] == word[-1])

print(count_words(["hello", "world", "python", "aardvark", "a"]))

# Output: 3

# Solution Explanation:
# The function 'count_words' takes a list of words as a parameter.
# The sum(1 for word in words if word[0] == word[-1]) generates a sum of 1 for each word in the list that starts and ends with the same letter.
# The function returns this sum.
<jupyter_output>
3
<jupyter_text>
Q3. Write a Python function to reverse words in a given string.
<jupyter_code>
# Python Solution:

def reverse_words(s):
    return ' '.join(word[::-1] for word in s.split())

print(reverse_words("hello world python"))

# Output: "olleh dlrow nohtyp"

# Solution Explanation: