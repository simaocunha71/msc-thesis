```
def find_even_pair(numbers):
    res = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] ^ numbers[j]) % 2 == 0:
                res += 1
    return res
```

