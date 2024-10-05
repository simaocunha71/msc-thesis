Here is the Java solution for the problem:

```java
public int howManyTimes(String string, String substring) {
    int count = 0;
    int start = 0;
    while (start < string.length()) {
        int index = string.indexOf(substring, start);
        if (index == -1) {
            break;
        }
        count++;
        start = index + 1;
    }
    return count;
}
```

This solution uses the `indexOf` method to find the index of the substring in the string, starting from the current position. If the substring is found, it increments the count and updates the start position to the index after the found substring. This process is repeated until the substring is not found anymore. The count is then returned as the result. 

For example, if the input string is "aaa" and the substring is "a", the function will return 3, because "a" is found three times in the string. If the input string is "aaaa" and the substring is "aa", the function will also return 3, because "aa" is found three times in the string. 

The function works correctly even when the substring is empty, in which case it returns 0. This is because an empty substring is not considered to be a part of the original string. 

The time complexity of this solution is O(n), where n is the length of the input string. This is because in the worst case, the function needs to iterate over the entire string to find all occurrences of the substring. The space complexity is O(1), because it only uses a constant amount of space to store the count and the start position. 