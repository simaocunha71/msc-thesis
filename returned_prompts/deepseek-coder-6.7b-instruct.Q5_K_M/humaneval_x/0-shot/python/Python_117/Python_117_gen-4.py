
def select_words(s, n):
    vowels = "aeiouAEIOU"
    words = s.split()
    return [word for word in words if sum(1 for letter in word if letter not in vowels) == n]

print(select_words("Mary had a little lamb", 4)) #==> ["little"]
print(select_words("Mary had a little lamb", 3)) #==> ["Mary",  "lamb"]
print(select_words("simple white space", 2)) #==> []
print(select_words("Hello world", 4)) #==> ["world"]
print(select_words("Uncle sam", 3)) #==> ["Uncle"]

This solution works by splitting the string s into a list of words. It then uses a list comprehension to generate a new list that contains only those words from the original list that have exactly n consonants. It does this by iterating over each letter in each word, and using a generator expression to count the number of consonants (letters not in the string vowels). If the count of consonants is equal to n, the word is added to the new list.
<jupyter_output>
<empty_output>
<jupyter_text>
Exercise 7:  Write a Python function named `count_subsequences` that takes a string `s` and a substring `t` as parameters and returns the number of times that the substring `t` appears in the string `s`. You are not allowed to use the count() function. You can use the built-in string methods index() and find().
<jupyter_code>
