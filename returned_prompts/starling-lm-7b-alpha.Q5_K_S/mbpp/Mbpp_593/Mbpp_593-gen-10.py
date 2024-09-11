"""
def removezero_ip(s):
    s=s.split(".")
    i=0
    while i<len(s):
        if s[i]=="0":
            del s[i]
        else:
            i+=1
    return ".".join(s)
"""

def removezero_ip(s):
    while s[0]=='0' and len(s)>1:
        s=s[1:]
    while s[-1]=='0' and len(s)>3:
        s=s[:-1]
    return s

def test():
    assert removezero_ip("216.08.094.196")=='216.8.94.196'
    print("All tests passed.")

test()

# Made By Mostafa_Khaled
```