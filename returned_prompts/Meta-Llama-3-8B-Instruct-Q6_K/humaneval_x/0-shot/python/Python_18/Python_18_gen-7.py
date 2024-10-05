def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

# Example usage:
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3

Note: The function uses a for loop to iterate over the characters in the string, and checks if the substring matches the current character. If it does, it increments the count. The function returns the count at the end. The example usage shows how to use the function with different inputs.