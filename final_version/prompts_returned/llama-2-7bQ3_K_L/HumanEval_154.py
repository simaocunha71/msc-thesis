
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    def rot(word,n):
        for i in range(n+1):
            word = ''.join([''.join([char] + list(map(chr,range(len(char)))) for char in word]) if (i%2) == 0 else [''.join([char]*3)] + [letter for letter in word]) for letter in word] )
        return word[::-1][1:-1]

    a = list(a)[1:]
    b = list(b)[1:]
    l=len(a)
    ml=len(b)
    if (ml<2):
        print("Must have at least 2 letters")
        return False
    if (ml>3 and a != b) :
        return True
    else:
        for i in range(1,5):
            #print(a[:i],b[:i])
            a=rot(a[:i-1],i*2) if not (b[:i] == rot(a[1:-i+1],i*2)) else b==rot(a[1:i],i*2)
            a=a[:i-1]
            #print(i,a[:i-1])
        #print("A",a[:l/4])
        #print("B",b[:ml/4])
        if (a == b):
            return True
        else:
            print("No matches found!")
            return False
        
"""
@cypc.py
cypc.py - 100%(243)
"""