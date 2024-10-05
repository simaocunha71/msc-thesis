Here is the Java code that solves the problem:

```java
public int countUpper(String s) {
    int count = 0;
    for (int i = 0; i < s.length(); i += 2) {
        char c = s.charAt(i);
        if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            count++;
        }
    }
    return count;
}
```

This code iterates through the string `s` by incrementing the index `i` by 2 each time. It checks if the character at the current index is an uppercase vowel ('A', 'E', 'I', 'O', 'U') and increments the count if it is. Finally, it returns the count.