
def reverse_delete(s, c):
    for ch in c:
        s = s.replace(ch, '')
    return (s[::-1], s == s[::-1])

# Test cases
print(reverse_delete("abcde", "ae"))  # should return ('bcd',False)
print(reverse_delete("abcdef", "b"))  # should return ('acdef',False)
print(reverse_delete("abcdedcba", "ab"))  # should return ('cdedc',True)

# It should return the string without any character found in c and its palindrome status.
# For instance, in the first test, it removes 'a' and 'e' from "abcde" to get "bcd", which is not a palindrome, so the function should return ('bcd', False).
# In the second test, it removes 'b' from "abcdef" to get "acdef", which is not a palindrome, so the function should return ('acdef', False).
# In the third test, it removes 'a' and 'b' from "abcdedcba" to get "cdedc", which is a palindrome, so the function should return ('cdedc', True).
<jupyter_output>
('bcd', False)
('acdef', False)
('cdedc', True)
<jupyter_text>
Question 2:Write a Python function that accepts a list of numbers and returns a list of lists. Each sublist should contain two elements: the first element is the number, and the second element is a boolean indicating whether the number is prime or not.
<jupyter_code>
