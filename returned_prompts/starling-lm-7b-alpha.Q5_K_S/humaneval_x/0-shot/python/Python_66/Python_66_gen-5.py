
def digitSum(s):
    s = filter(lambda x: x.isupper(), s)
    return sum(map(lambda x: ord(x), s))

#tests
print(digitSum("")) # 0
print(digitSum("abAB")) # 131
print(digitSum("abcCd")) # 67
print(digitSum("helloE")) # 69
print(digitSum("woArBld")) # 131
print(digitSum("aAaaaXa")) # 153


# Other solutions:

def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())

#tests
print(digitSum("")) # 0
print(digitSum("abAB")) # 131
print(digitSum("abcCd")) # 67
print(digitSum("helloE")) # 69
print(digitSum("woArBld")) # 131
print(digitSum("aAaaaXa")) # 153
```
    
    
    
    
   digitSum = lambda s: sum(ord(c) for c in s if c.isupper())
    #tests
    print(digitSum("")) # 0
    print(digitSum("abAB")) # 131
    print(digitSum("abcCd")) # 67
    print(digitSum("helloE")) # 69
    print(digitSum("woArBld")) # 131
    print(digitSum("aAaaaXa")) # 153

```

```
    
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())

#tests
print(digitSum("")) # 0
print(digitSum("abAB")) # 131
print(digitSum("abcCd")) # 67
print(digitSum("helloE")) # 69
print(digitSum("woArBld")) # 131