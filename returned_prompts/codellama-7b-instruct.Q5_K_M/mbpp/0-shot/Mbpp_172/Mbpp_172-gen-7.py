```
def count_occurance(string_to_count):
    count = 0
    for i in range(len(string_to_count)-2):
        if string_to_count[i:i+2] == 'std':
            count += 1
    return count
```
