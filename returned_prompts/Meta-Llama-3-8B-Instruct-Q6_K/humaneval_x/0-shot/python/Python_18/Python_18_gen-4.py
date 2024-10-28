```
def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string_length = len(string)

    for i in range(string_length):
        if string[i:i + substring_length] == substring:
            count += 1
    return count
```


The function `how_many_times` takes two parameters, `string` and `substring`. It counts the occurrences of the `substring` in the `string`, considering overlapping matches. The function uses a for loop to iterate over the `string` and checks if the current substring matches the `substring`. If it does, it increments the `count`. Finally, it returns the `count`. The time complexity is O(n*m) where n is the length of the string and m is the length of the substring. The space complexity is O(1) as it only uses a constant amount of space. The function is tested with some examples and works as expected.