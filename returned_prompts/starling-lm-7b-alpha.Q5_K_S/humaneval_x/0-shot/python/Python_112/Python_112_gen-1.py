
def reverse_delete(s,c):
    result = ""
    for i in s:
        if i not in c:
            result += i
    if result == result[::-1]:
        return (result,"True")
    else:
        return (result,"False")


# Test
print(reverse_delete("abcde","ae"))  # ('bcd', False)
print(reverse_delete("abcdef","b"))  # ('acdef', False)
print(reverse_delete("abcdedcba","ab"))  # ('cdedc', True)
print(reverse_delete("abcde","ae"))  # ('bcd', False)


























```