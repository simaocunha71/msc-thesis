    result = [char for char in s if char not in c]
    is_palindrome = result == result[::-1]
    return (''.join(result), is_palindrome)  # return result string and palindrome check as a tuple
# Example usage:
s = "abcdedcba"
c = "ab"
print(reverse_delete(s, c))  # Output: ('cdedc', True)
# Example usage:
s = "abcde"
c = "ae"
print(reverse_delete(s, c))  # Output: ('bcd', False)  # result string and palindrome check as a tuple
# Example usage:
s = "abcdef"
c = "b"
print(reverse_delete(s, c))  # Output: ('acdef', False)  # result string and palindrome check as a tuple
# Example usage:
s = "abcdedcba"
c = "ab"
print(reverse_delete(s, c))  # Output: ('cdedc', True)  # result string and palindrome check as a tuple
# Example usage:
s = "abcde"
c = "ae"
print(reverse_delete(s, c))  # Output: ('bcd', False)  # result string and palindrome check as a tuple
# Example usage:
s = "abcdef"
c = "b"
print(reverse_delete(s, c))  # Output: ('acdef', False)  # result string and palindrome check as a tuple
# Example usage:
s = "abcdedcba"
c = "ab"
print(reverse_delete(s, c))  # Output: ('cdedc', True)  # result string and palindrome check as a tuple
# Example usage:
s = "abcde"
c = "ae"
print(reverse_delete(s, c))  # Output: ('bcd', False)  # result string and palindrome check as a tuple
# Example usage:
s = "abcdef"
c = "b"
print(reverse_delete(s, c))  # Output: ('acdef', False)  # result string and palindrome check as a tuple
# Example usage:
s = "abcdedcba"
c = "ab"
print(reverse_delete(s, c))  # Output: ('cdedc', True)  # result string and palindrome check as a tuple
# Example usage:
s = "abcde"
c = "ae"
print(reverse_delete(s, c))  # Output: ('bcd', False)  # result string and palindrome check as a tuple
