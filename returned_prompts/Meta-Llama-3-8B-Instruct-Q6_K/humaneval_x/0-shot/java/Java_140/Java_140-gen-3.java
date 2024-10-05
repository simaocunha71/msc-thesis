Here is the Java solution for the problem:

```java
public String fixSpaces(String text) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < text.length(); i++) {
        if (text.charAt(i) == ' ') {
            if (sb.length() > 0 && sb.charAt(sb.length() - 1) == ' ') {
                if (sb.length() > 2) {
                    sb.append('-');
                }
            } else {
                sb.append('_');
            }
        } else {
            sb.append(text.charAt(i));
        }
    }
    return sb.toString();
}
```

This solution iterates over the input string and checks each character. If the character is a space, it checks if the last character in the StringBuilder is also a space. If it is, it checks if the StringBuilder has more than 2 characters. If it does, it appends a '-' to the StringBuilder. If the last character in the StringBuilder is not a space, it appends an '_' to the StringBuilder. If the character is not a space, it simply appends it to the StringBuilder. Finally, it returns the string representation of the StringBuilder.