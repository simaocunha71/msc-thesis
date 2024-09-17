```
def validate(n):
    freq = [0] * 10
    while n > 0:
        digit = n % 10
        freq[digit] += 1
        n //= 10
    for i in range(10):
        if freq[i] > i:
            return False
    return True
```

This function works by first initializing a frequency list of 10 elements, all set to 0. Then it iterates over the digits of the input number, incrementing the corresponding frequency in the list for each digit. Finally, it checks each frequency in the list to make sure it's less than or equal to the digit it corresponds to. If any frequency is greater, it returns False. If it gets through the loop without finding any frequencies greater than their corresponding digits, it returns True.