
def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """

    res_str=""
    for ch in c:
        while ch[0] == ch[-1]:
            if ch[:-1]==ch+"e":
                break
        else:
            res_str+=ch[:-1]+" "
    if len(res_str)%2 != 0:
        return None, False
    str=res_str[::-1]
    if str==res_str[:]:
        return (str,"True")
    else :return None,False
