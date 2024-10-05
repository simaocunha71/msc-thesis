Here is the Java code that solves the problem:

```java
public String fixSpaces(String text) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < text.length(); i++) {
        char c = text.charAt(i);
        if (c == ' ') {
            if (sb.length() > 0 && sb.charAt(sb.length() - 1) == ' ') {
                if (sb.length() > 2) {
                    sb.append('-');
                }
            } else {
                sb.append('_');
            }
        } else {
            sb.append(c);
        }
    }
    return sb.toString();
}
```
This code uses a StringBuilder to build the resulting string. It iterates over the input string, and for each character:
- If the character is a space, it checks if the last character in the StringBuilder is also a space. If it is, and the StringBuilder has more than 2 characters, it appends a '-' to the StringBuilder. Otherwise, it appends an underscore.
- If the character is not a space, it simply appends it to the StringBuilder.
Finally, it returns the resulting string. This solution has a time complexity of O(n), where n is the length of the input string.