```
def odd_Equivalent(binary_string, rotations):
    binary_string = binary_string * (rotations // len(binary_string) + 1)
    return binary_string.count('1')
```
