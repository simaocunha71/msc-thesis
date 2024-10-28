    def check(s1,s2):
        if s2 in s1:
            return True
        for i in range(len(s1)-len(s2)):
            if s2[1:]==s1[i+1:i+len(s2)]:
                return True
        return False

    return check(a,b)


#cycpattern_check("abab","baa")













```