
def reverse_delete(s,c):
    new_s = ""
    for i in s:
        if i not in c:
            new_s += i
    if new_s == new_s[::-1]:
        return (new_s,True)
    else:
        return (new_s,False)


print(reverse_delete("abcde", "ae"))
print(reverse_delete("abcdef", "b"))
print(reverse_delete("abcdedcba", "ab"))




# Python program to delete all the characters from string 's' which are present in string 'c' and then check if the resultant string is palindrome or not.

def reverse_delete(s,c):
    # Deleting all the characters from 's' which are present in 'c'
    for i in c:
        s = s.replace(i,"")

    # Checking if the resultant string is palindrome or not
    if s == s[::-1]:
        return (s,True)
    else:
        return (s,False)


print(reverse_delete("abcde", "ae"))
print(reverse_delete("abcdef", "b"))
print(reverse_delete("abcdedcba", "ab"))






















































```