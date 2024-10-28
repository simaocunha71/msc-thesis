Here is the Java code that solves the problem:

```java
public String fixSpaces(String text) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < text.length(); i++) {
        if (text.charAt(i) == ' ') {
            if (sb.length() > 0 && sb.charAt(sb.length() - 1) == ' ') {
                if (sb.length() > 1 && sb.charAt(sb.length() - 2) == ' ') {
                    sb.append('-');
                } else {
                    sb.append('_');
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

This code iterates over the input string `text`. If the current character is a space, it checks if the previous character was also a space. If it was, it checks if the character before that was also a space. If it was, it appends a `-` to the `StringBuilder`. If not, it appends an `_`. If the current character is not a space, it simply appends it to the `StringBuilder`. Finally, it returns the string representation of the `StringBuilder`. This solution has a time complexity of O(n), where n is the length of the input string. 