```
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    return count
```
This function iterates over the string and checks if the substring is found at each position. If it is, it increments the count. The `startswith` method is used to check if the substring is found at each position. The `range` function generates the indices of the string, and the `len` function is used to get the length of the string. The function returns the total count of the substring found in the string. 

The time complexity of this function is O(n*m) where n is the length of the string and m is the length of the substring. This is because in the worst case, the function has to iterate over the entire string and check if the substring is found at each position. 

The space complexity of this function is O(1) as it only uses a constant amount of space to store the count and indices. 





