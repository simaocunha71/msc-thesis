
def reverse_delete(s,c):
    s1 = ""
    for i in s:
        if i not in c:
            s1 += i
    if s1 == s1[::-1]:
        return (s1,True)
    else:
        return (s1,False)


# print(reverse_delete("abcdedcba","ab"))
# print(reverse_delete("abcdef","b"))
# print(reverse_delete("abcde","ae"))










```