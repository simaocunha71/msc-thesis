/*
Find how many times a given substring can be found in the original string. Count overlaping cases.
>>> how_many_times("", "a")
0
>>> how_many_times("aaa", "a")
3
>>> how_many_times("aaaa", "aa")
3
*/
def how_many_times(str, substring):
    if len(str) == 0 or len(substring) == 0:
        return 0
    count = 0
    for i in range(len(str) - len(substring) + 1):
        if str[i:i+len(substring)] == substring:
            count += 1
    return count

B:
/*
Find how many times a given substring can be found in the original string. Count overlaping cases.
>>> how_many_times("", "a")
0
>>> how_many_times("aaa", "a")
3
>>> how_many_times("aaaa", "aa")
3
*/
def how_many_times(str, substring):
    count = 0
    for i in range(len(str)):
        if str[i:i+len(substring)] == substring:
            count += 1
    return count

C:
/*
Find how many times a given substring can be found in the original string. Count overlaping cases.
>>> how_many_times("", "a")
0
>>> how_many_times("aaa", "a")
3
>>> how_many_times("aaaa", "aa")
3
*/
def how_many_times(str, substring):
    count = 0
    for i in range(len(str) - len(substring) + 1):
        if str[i:i+len(substring)] == substring:
            count += 1
    return count

D:
/*
Find how many times a given substring can be found in the original string. Count overlaping cases.
>>> how_many_times("", "a")
0
>>> how_many_times("aaa", "a")
3
>>> how_many_times("aaaa", "aa")
3
*/
def how_many_times(str, substring):
    count = 0
    for i in range(len(str) - len(substring) + 1):
        if str[i:i+len(substring)] == substring:
            count += 1
    return count

E:
/*
Find how many times a given substring can be found in the original string. Count overlaping cases.
>>> how_many_times("", "a")
0
>>> how_many_times("aaa", "a")
3
>>> how_many_times("aaaa", "aa")
3
