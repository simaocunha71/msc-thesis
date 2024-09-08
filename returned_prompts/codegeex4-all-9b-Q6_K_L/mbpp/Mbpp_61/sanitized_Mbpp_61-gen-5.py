def count_Substrings(s):
    def dfs(i, path, total):
        if i == len(s):
            if total == len(path):
                return 1
            else:
                return 0
        else:
            return dfs(i + 1, path + [s[i]], total + int(s[i])) + dfs(i + 1, path, total)

    return dfs(0, [], 0)