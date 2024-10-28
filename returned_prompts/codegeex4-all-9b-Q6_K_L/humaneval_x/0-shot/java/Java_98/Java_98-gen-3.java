```java
public int countUpper(String s) {
    int count = 0;
    for (int i = 0; i < s.length(); i += 2) {
        if (i < s.length()) {
            char c = s.charAt(i);
            if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                count++;
            }
        }
    }
    return count;
}
```
This solution iterates through the string `s` with a step size of 2, checking if each character is an uppercase vowel. If it is, the count is incremented. The method returns the final count.