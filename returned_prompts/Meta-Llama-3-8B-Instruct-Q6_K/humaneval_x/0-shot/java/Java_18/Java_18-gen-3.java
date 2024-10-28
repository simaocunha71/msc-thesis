Here is a simple Java solution that uses the `indexOf` method to find the index of the substring in the string, and then uses a loop to count the number of occurrences.

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

This method works by starting at the beginning of the string and searching for the substring. When it finds the substring, it increments the count and moves the index to the end of the substring. It then repeats this process until it no longer finds the substring. The result is the total number of times the substring appears in the string.

For example, if you call `howManyTimes("aaa", "a")`, the method will return 3, because the substring "a" appears three times in the string "aaa". If you call `howManyTimes("aaaa", "aa")`, the method will also return 3, because the substring "aa" appears three times in the string "aaaa". If you call `howManyTimes("", "a")`, the method will return 0, because the substring "a" does not appear at all in the empty string.