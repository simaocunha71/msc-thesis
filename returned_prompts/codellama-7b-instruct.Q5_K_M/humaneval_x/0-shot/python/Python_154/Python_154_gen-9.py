
def cycpattern_check(a , b):
    #your code here
    if len(a) != len(b):
        return False
    for i in range(len(b)):
        if b in a:
            return True
        b = b[1:] + b[0]
    return False

#a = "abcd"
#b = "abd"
#print(cycpattern_check(a,b))
#

def cycpattern_check(a , b):
    #your code here
    if len(a) != len(b):
        return False
    for i in range(len(b)):
        if b in a:
            return True
        b = b[1:] + b[0]
    return False

#a = "hello"
#b = "ell"
#print(cycpattern_check(a,b))

#a = "whassup"
#b = "psus"
#print(cycpattern_check(a,b))
#
#a = "abab"
#b = "baa"
#print(cycpattern_check(a,b))

#a = "efef"
#b = "eeff"
#print(cycpattern_check(a,b))

#a = "himenss"
#b = "simen"
#print(cycpattern_check(a,b))

#a = "himenss"
#b = "simen"
#print(cycpattern_check(a,b))

#a = "abcd"
#b = "abd"
#print(cycpattern_check(a,b))

#a = "hello"
#b = "ell"
#print(cycpattern_check(a,b))

#a = "whassup"
#b = "psus"
#print(cycpattern_check(a,b))

#a = "abab"
#b = "baa"
#print(cycpattern_check(a,b))

#a = "efef"
#b = "eeff"
#print(cycpattern_check(a,b))

