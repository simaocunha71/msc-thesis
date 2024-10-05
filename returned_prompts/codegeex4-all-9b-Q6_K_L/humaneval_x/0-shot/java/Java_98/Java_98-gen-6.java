You can iterate through the string with a for loop, checking if the character at the current index is an uppercase vowel (A, E, I, O, U) and if the index is even. If both conditions are met, increment a counter variable. Finally, return the counter.

Here's a possible implementation:

```java
public int countUpper(String s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (i % 2 == 0 && (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')) {
            count++;
        }
    }
    return count;
}
```

This implementation loops through the string s, and for each character, it checks if the index is even and if the character is an uppercase vowel. If both conditions are met, the count is incremented. Finally, the count is returned.