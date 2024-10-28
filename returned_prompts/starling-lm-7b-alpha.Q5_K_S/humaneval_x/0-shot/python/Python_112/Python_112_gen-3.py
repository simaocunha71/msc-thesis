
def reverse_delete(s,c):
    s = list(s)
    for i in range(len(s)):
        if s[i] in c:
            s.pop(i)
    if s == s[::-1]:
        return ("".join(s),True)
    else:
        return ("".join(s),False)

# def reverse_delete(s,c):
#     s = list(s)
#     for i in range(len(s)-1,-1,-1):
#         if s[i] in c:
#             s.pop(i)
#     if s == s[::-1]:
#         return ("".join(s),True)
#     else:
#         return ("".join(s),False)



if __name__ == "__main__":
    print(reverse_delete("abcde","ae"))
    print(reverse_delete("abcdef","b"))
    print(reverse_delete("abcdedcba","ab"))

```

```
('bcd', False)
('acdef', False)
('cdedc', True)
```
