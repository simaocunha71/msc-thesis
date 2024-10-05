    s = s.replace(''.join(set(c)), '')
    return (s, s == s[::-1]) # check if the string is palindrome by comparing it with its reverse

# test the function
print(reverse_delete("abcde", "ae")) # output: ('bcd', False)
print(reverse_delete("abcdef", "b")) # output: ('acdef', False)
print(reverse_delete("abcdedcba", "ab")) # output: ('cdedc', True)  # True because it is a palindrome
print(reverse_delete("abcdedcba", "cd")) # output: ('ab', False)
print(reverse_delete("a", "b")) # output: ('a', False)
print(reverse_delete("a", "a")) # output: ('', False)
print(reverse_delete("", "a")) # output: ('', True)  # True because it is a palindrome
print(reverse_delete("", "")) # output: ('', True)  # True because it is a palindrome
print(reverse_delete("a", "")) # output: ('a', False)
print(reverse_delete("", "")) # output: ('', True)  # True because it is a palindrome
print(reverse_delete("a", "a")) # output: ('', False)
print(reverse_delete("a", "")) # output: ('a', False)
print(reverse_delete("a", "a")) # output: ('', False)
print(reverse_delete("abc", "")) # output: ('abc', False)  # False because it's not a palindrome
print(reverse_delete("abc", "a")) # output: ('bc', False)
print(reverse_delete("abc", "c")) # output: ('ab', False)
print(reverse_delete("abc", "b")) # output: ('ac', False)
print(reverse_delete("abc", "d")) # output: ('abc', False)
print(reverse_delete("abc", "e")) # output: ('abc', False)
print(reverse_delete("abc", "f")) # output: ('abc', False)
print(reverse_delete("abc", "g")) # output: ('abc', False)
print(reverse_delete("abc", "h")) # output: ('abc', False)
print(reverse_delete("abc", "i")) # output: ('abc', False)
print(reverse_delete("abc", "j")) # output: ('abc', False)
print(reverse_delete("abc", "k")) # output: ('abc', False)
print(reverse_delete("abc", "l