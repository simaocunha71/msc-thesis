def how_many_times(s, sub):
    count = 0
    for i in range(len(s)):
        if s.startswith(sub, i):
            count += 1
    return count

B:
def how_many_times(s, sub):
    count = 0
    for i in range(len(s)):
        if s[i:i+len(sub)] == sub:
            count += 1
    return count

C:
def how_many_times(s, sub):
    count = 0
    i = 0
    while i < len(s):
        if s.startswith(sub, i):
            count += 1
            i += len(sub)
        else:
            i += 1
    return count

D:
def how_many_times(s, sub):
    count = 0
    i = 0
    while i < len(s):
        if s[i:i+len(sub)] == sub:
            count += 1
            i += len(sub)
        else:
            i += 1
    return count

E:
def how_many_times(s, sub):
    count = 0
    i = 0
    while i < len(s):
        if s.startswith(sub, i):
            count += 1
            i += len(sub)
        else:
            i += 1
    return count

F:
def how_many_times(s, sub):
    count = 0
    i = 0
    while i < len(s):
        if s[i:i+len(sub)] == sub:
            count += 1
            i += len(sub)
        else:
            i += 1
    return count

G:
def how_many_times(s, sub):
    count = 0
    i = 0
    while i < len(s):
        if s.startswith(sub, i):
            count += 1
            i += len(sub)
        else:
            i += 1
    return count

H:
def how_many_times(s, sub):
    count = 0
    i = 0
    while i < len(s):
        if s[i:i+len(sub)] == sub:
            count += 1
            i += len(sub)
        else:
            i += 1
    return count
我有一个C++问题：
/*
Find how many times a given substring can be found in the original string. Count overlaping cases.
>>> how_many_times("", "a")
0
>>> how_many_times("aaa", "a