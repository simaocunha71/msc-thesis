
def reverse_delete(s,c):
    s=list(s)
    for i in c:
        s.remove(i)
    if s==s[::-1]:
        return (s,True)
    else:
        return (s,False)

# print(reverse_delete("abcde", "ae"))
# print(reverse_delete("abcdef", "b"))
# print(reverse_delete("abcdedcba", "ab"))








```