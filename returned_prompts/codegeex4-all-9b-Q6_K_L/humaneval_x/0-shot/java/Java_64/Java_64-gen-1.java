Here is a Java solution for the problem:

```java
public int vowelsCount(String s) {
    int count = 0;
    s = s.toLowerCase();

    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            count++;
        }
    }

    if (s.endsWith("y")) {
        count++;
    }

    return count;
}
```

Explanation:
The function `vowelsCount` first converts the input string to lowercase to handle case-insensitivity. Then, it iterates over each character in the string. If the character is a vowel (i.e., 'a', 'e', 'i', 'o', or 'u'), it increments the count. After the loop, it checks if the string ends with 'y' and if so, increments the count. Finally, it returns the count of vowels in the string.