
def get_row(lst, x):
    ans = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                ans.append((i, j))
    ans.sort(key=lambda x: x[0])
    ans.sort(key=lambda x: x[1], reverse=True)
    return ans
