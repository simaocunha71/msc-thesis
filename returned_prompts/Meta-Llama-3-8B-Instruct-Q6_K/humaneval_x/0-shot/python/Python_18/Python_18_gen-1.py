    def how_many_times(string: str, substring: str) -> int:
        count = start = 0
        while start < len(string):
            pos = string.find(substring, start)
            if pos != -1:
                start = pos + 1
                count += 1
            else:
                break
        return count
    # Test cases
    print(how_many_times('', 'a'))  # 0
    print(how_many_times('aaa', 'a'))  # 3
    print(how_many_times('aaaa', 'aa'))  # 3

Output:
0
3
3

Explanation:
The provided function `how_many_times` counts the occurrences of a given substring within a string. It uses the `find` method to locate the substring in the string, starting from the current position (`start`). If the substring is found, it increments the count and moves the start position to the end of the found substring plus one. This ensures that overlapping occurrences are also counted. If the substring is not found, the function breaks the loop and returns the count. The function is tested with the provided test cases, which demonstrate its functionality.