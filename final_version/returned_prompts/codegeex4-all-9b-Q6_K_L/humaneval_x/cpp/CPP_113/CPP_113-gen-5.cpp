def odd_count(lst):
    res = []
    for num in lst:
        count = 0
        for digit in num:
            if int(digit) % 2 != 0:
                count += 1
        res.append('the number of odd elements in the string {} of the input.'.format(count))
    return res

print(odd_count(["1234567"]))
print(odd_count(["3","11111111"]))
```


