def long_words(n, sentence):
    words = sentence.split(" ")
    long_words = [word for word in words if len(word) > n]
    return long_words

print(long_words(3, "python is a programming language"))

# Output: ['python', 'programming', 'language']

# Explanation: The function takes two parameters, the length 'n' and the sentence. It first splits the sentence into words. 
# Then it uses a list comprehension to create a list of words that are longer than 'n' characters. Finally, it returns this list of long words.
<jupyter_output>
['python', 'programming', 'language']
<jupyter_text>
Question 3: Write a Python function that takes a list of integers as an input and returns the sum of the squares of all the even numbers in the list.
<jupyter_code>
