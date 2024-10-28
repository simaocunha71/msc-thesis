
def reverse_delete(s,c):
    result = "".join(ch for ch in s if ch not in c)
    return (result, result == result[::-1])

# Test cases
print(reverse_delete("abcde", "ae"))  # should return ('bcd', False)
print(reverse_delete("abcdef", "b"))  # should return ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # should return ('cdedc', True)

# Explanation:
# In the first test case, 'a' and 'e' are removed from "abcde" so we get "bcd". It is not a palindrome because it reads "bcd" backward not forward.
# In the second test case, 'b' is removed from "abcdef" so we get "acdef". It is still not a palindrome because it reads "acdef" backward not forward.
# In the third test case, 'a' and 'b' are removed from "abcdedcba" so we get "cdedc". It is a palindrome because it reads "cdedc" both backward and forward.
<jupyter_output>
('bcd', False)
('acdef', False)
('cdedc', True)
<jupyter_text>
Question 3:Write a Python function named "count_substring" that takes two arguments: a string "s" and a substring "t". The function should return the number of occurrences of the substring "t" in string "s".
<jupyter_code>
