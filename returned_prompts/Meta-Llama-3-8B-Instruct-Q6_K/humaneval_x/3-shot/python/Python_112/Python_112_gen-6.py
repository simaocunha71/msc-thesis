    s_list = list(s)
    for char in c:
        try:
            s_list.remove(char)
        except ValueError:
            pass
    s = ''.join(s_list)
    return s, s == s[::-1] # check if the string is palindrome
# example:
print(reverse_delete("abcde", "ae")) # ('bcd',False)
print(reverse_delete("abcdef", "b")) # ('acdef',False)
print(reverse_delete("abcdedcba", "ab")) # ('cdedc',True)