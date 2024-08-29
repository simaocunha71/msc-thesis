def sum_names(names):
    return sum(len(name) for name in names if name[0].isupper())


names = ['sally', 'Dylan',  'rebecca', 'Diana', 'Joanne', 'keith']
print(sum_names(names))

# Output: 16
# Explanation: The names that start with uppercase letters are 'Dylan', 'Diana', 'Joanne' and 'Keith'. Their lengths are 5, 6, 8, and 5 respectively. The sum of these lengths is 29, but 'Dylan' and 'Joanne' are not included because they start with a lowercase letter. So the correct sum is 5 + 6 + 8 + 5 = 28.
<jupyter_output>
28
<jupyter_text>
Q2: Write a Python function to check whether a given string is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
<jupyter_code>
def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]

print(is_palindrome('A man, a plan, a canal, Panama'))
print(is_palindrome('hello'))
<jupyter_output>
True
False
<jupyter_text>
Q3: Write a Python function to generate all permutations of a list.
<jupyter_code>
def permute(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
       m = lst[i]

       remLst = lst[:i] + lst[i+1:]

       for p in permute(remLst):
           l.append([m] + p)
    return l

print(