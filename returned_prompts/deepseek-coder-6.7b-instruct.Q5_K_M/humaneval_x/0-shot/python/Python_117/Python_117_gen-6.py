
    def select_words(s, n):
        if not s:
            return []

        vowels = "aeiouAEIOU"
        words = s.split()
        result = []

        for word in words:
            count = 0
            for letter in word:
                if letter not in vowels:
                    count += 1
            if count == n:
                result.append(word)

        return result

print(select_words("Mary had a little lamb", 4))
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))


"""
Output:
['little']
['Mary', 'lamb']
[]
['world']
['Uncle']
"""

Explanation:

The function 'select_words' takes in two parameters, a string 's' and a number 'n'.
It first checks if the string is empty. If it is, it returns an empty list.
Then it splits the string 's' into words using the split method and initializes an empty list 'result'.
Next, it iterates through each word in the list of words. For each word, it counts the number of consonants by checking if the letter is not in the string of vowels. If the count of consonants equals 'n', it appends the word to the list 'result'.
Finally, it returns the list 'result'.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 19:
<jupyter_code>
