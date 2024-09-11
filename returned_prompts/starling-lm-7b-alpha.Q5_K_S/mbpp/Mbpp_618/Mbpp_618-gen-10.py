def longest_string(words):
    if len(words)==0:
        return None
    else:
        res=words[0]
        for i in range(len(words)):
            if len(words[i])>len(res):
                res=words[i]
        return res

"""
Given a string, return the length of the string

Examples:
assert length