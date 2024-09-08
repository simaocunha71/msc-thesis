def anti_shuffle(s):
    s = s.split()
    for i in range(len(s)):
        s[i] = "".join(sorted(s[i]))
    return " ".join(s)
print(anti_shuffle('Hello World!!!'))
print(anti_shuffle('hello'))
print(anti_shuffle('Hi'))