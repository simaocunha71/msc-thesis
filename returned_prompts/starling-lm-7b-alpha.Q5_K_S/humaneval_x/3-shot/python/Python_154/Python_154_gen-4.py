    def rotate(s, n):
        return s[n:] + s[:n]
    def isSubstring(s1, s2):
        for i in range(len(s1)):
            if s2 == s1[i:]:
                return True
        return False
    a = a.lower()
    b = b.lower()
    for i in range(len(b)):
        if isSubstring(a,b[i:]):
            return True
    for i in range(len(b)):
        if isSubstring(a,rotate(b,i)):
            return True
    return False



