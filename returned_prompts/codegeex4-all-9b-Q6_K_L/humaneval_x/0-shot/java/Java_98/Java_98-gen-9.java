Here is a Java solution to your problem:

```java
public int countUpper(String s) {
    int count = 0;
    for(int i = 0; i < s.length(); i += 2) {
        char c = s.charAt(i);
        if(c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            count++;
        }
    }
    return count;
}
```

This solution iterates through the string `s` at even indices (0, 2, 4, ...). If the character at the current index is an uppercase vowel (A, E, I, O, U), it increments the count. Finally, it returns the count.