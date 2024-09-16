```
def odd_values_string(input_string):
    return ''.join([char for index, char in enumerate(input_string) if index % 2 == 0])
```
