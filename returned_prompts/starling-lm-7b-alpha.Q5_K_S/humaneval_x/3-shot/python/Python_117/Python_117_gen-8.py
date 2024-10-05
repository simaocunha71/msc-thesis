    vowels = set("aeiou")
    def consonants(s):
        return sum(1 for c in s if c.isalpha() and c not in vowels)

    def helper(s, n):
        result = []
        idx = 0
        while idx < len(s):
            idx2 = idx
            while idx2 < len(s) and s[idx2] != " ":
                idx2 += 1
            if consonants(s[idx:idx2]) == n:
                result.append(s[idx:idx2])
            idx = idx2 + 1
        return result

    return helper(s, n)


