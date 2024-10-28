Here is a simple solution using the `indexOf` method and a loop:

```java
public int howManyTimes(String string, String substring) {
    int count = 0;
    int index = 0;
    while ((index = string.indexOf(substring, index)) != -1) {
        count++;
        index += substring.length();
    }
    return count;
}
```

This method works by starting at the beginning of the string and searching for the substring. If the substring is found, the count is incremented and the search is continued from the end of the previous match. This continues until the substring is no longer found in the string. The result is the number of times the substring appears in the string. 

For example, if you call `howManyTimes("aaa", "a")`, it will return 3 because "a" appears three times in the string "aaa". Similarly, `howManyTimes("aaaa", "aa")` will return 3 because "aa" appears three times in the string "aaaa". 

If the substring is an empty string, the method will return 0 because an empty string is not considered a match. 

This method is case-sensitive and does not handle overlapping matches. If you need to handle overlapping matches, you can modify the method to keep track of the last position where the substring was found and start the next search from that position. 

Here's an updated version of the method that handles overlapping matches:

```java
public int howManyTimes(String string, String substring) {
    int count = 0;
    int index = 0;
    while ((index = string.indexOf(substring, index)) != -1) {
        count++;
        index += 1; // Start searching from the next character
    }
    return count;
}
```

In this version, the `index` variable is incremented by 1 after each match, so the next search starts from the next character in the string. This ensures that overlapping matches are counted correctly. 

For example, if you call `howManyTimes("aaa", "a")`, it will return 3 because "a" appears three times in the string "aaa", including the overlapping match. Similarly, `howManyTimes("aaaa", "aa")` will return 3 because "aa" appears three times in the string "aaaa", including the overlapping matches. 