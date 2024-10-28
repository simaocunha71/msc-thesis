Here is the solution in Java:

```java
public int howManyTimes(String string, String substring) {
    if (substring.isEmpty()) {
        return 0;
    }
    int count = 0;
    int start = 0;
    while (start < string.length()) {
        int pos = string.indexOf(substring, start);
        if (pos != -1) {
            count++;
            start = pos + substring.length();
        } else {
            break;
        }
    }
    return count;
}
```

This solution uses a while loop to find all occurrences of the substring in the string. It starts by initializing the count to 0 and the start position to 0. Then it enters a loop where it checks for the substring at the current start position using the `indexOf` method. If it finds the substring, it increments the count and moves the start position to the end of the found substring. If it doesn't find the substring, it breaks out of the loop. Finally, it returns the count of found substrings.

The time complexity of this solution is O(n), where n is the length of the string, because in the worst case, it needs to iterate over the entire string. The space complexity is O(1), because it only uses a constant amount of space to store the count and the start position.