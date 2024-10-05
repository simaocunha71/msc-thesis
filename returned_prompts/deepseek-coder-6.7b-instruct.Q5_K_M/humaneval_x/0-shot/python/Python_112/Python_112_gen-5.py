
def reverse_delete(s, c):
    result = ''.join(ch for ch in s if ch not in c)
    return (result, result == result[::-1])

print(reverse_delete("abcde", "ae"))
print(reverse_delete("abcdef", "b"))
print(reverse_delete("abcdedcba", "ab"))

# This function works by iterating over each character in the string 's' and checking if it is in the string 'c'. If it is not, it is included in the new string. The new string is then checked if it is a palindrome by comparing it to its reverse (obtained by slicing with a step of -1). The function returns the result string and a boolean indicating whether it is a palindrome.
<jupyter_output>
('bcd', False)
('acdef', False)
('cdedc', True)
<jupyter_text>
