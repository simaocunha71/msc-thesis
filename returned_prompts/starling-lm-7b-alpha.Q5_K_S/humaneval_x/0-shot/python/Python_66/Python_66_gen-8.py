
def digitSum(s):
    sum = 0
    for i in s:
        if i.isupper():
            sum += ord(i)
    return sum

# Test
print(digitSum("")) # 0
print(digitSum("abAB")) # 131
print(digitSum("abcCd")) # 67
print(digitSum("helloE")) # 69
print(digitSum("woArBld")) # 131
print(digitSum("aAaaaXa")) # 153


# Using for loop, check if the character is upper, if true, add it's ASCII code to sum

# In Python, the ASCII codes are from 0 to 127
# A is 65, B is 66, C is 67, ...
# For upper characters, their ASCII codes are consecutive
# So we can use ord(i) to get the ASCII code of the character i

# The sum of all upper characters' ASCII codes is the answer

```
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

