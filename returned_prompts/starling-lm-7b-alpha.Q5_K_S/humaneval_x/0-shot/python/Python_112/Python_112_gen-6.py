
def reverse_delete(s,c):
    s1 = ""
    for i in s:
        if i not in c:
            s1 += i
    if s1 == s1[::-1]:
        return (s1,True)
    else:
        return (s1,False)

# def reverse_delete(s,c):
#     l = []
#     for i in s:
#         if i not in c:
#             l.append(i)
#     if l == l[::-1]:
#         return (s1,True)
#     else:
#         return (s1,False)



s = "abcdedcba"
c = "ab"
print(reverse_delete(s,c))












```
