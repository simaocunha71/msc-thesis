"""
def Find_Min(s):
    mini = len(s[0])
    for i in s:
        if len(i) < mini:
            mini = len(i)
    return mini

s = [[1],[1,2],[1,2,3]]
print(Find_Min(s))
"""

