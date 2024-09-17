def add_string(L,s):
    ans = []
    for i in L:
        ans.append(s.format(i))
    return ans