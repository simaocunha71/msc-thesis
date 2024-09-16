```
def find_Rotations(string):
    count = 0
    for i in range(len(string)):
        if string[i] != string[0]:
            count += 1
    return count
```
