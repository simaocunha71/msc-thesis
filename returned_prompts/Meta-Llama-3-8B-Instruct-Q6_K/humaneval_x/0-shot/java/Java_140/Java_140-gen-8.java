Here is the solution in Java:

```java
public String fixSpaces(String text) {
    StringBuilder result = new StringBuilder();
    for (int i = 0; i < text.length(); i++) {
        if (text.charAt(i) == ' ') {
            if (result.length() > 0 && result.charAt(result.length() - 1) == ' ') {
                if (result.length() > 2 && result.charAt(result.length() - 3) == ' ') {
                    result.append('-');
                } else {
                    result.append('_');
                }
            } else {
                result.append('_');
            }
        } else {
            result.append(text.charAt(i));
        }
    }
    return result.toString();
}
```
This solution iterates over the input string character by character. When it encounters a space, it checks if the previous character was also a space. If it was, it checks if the character before that was also a space. If it was, it appends a `-` to the result. Otherwise, it appends an underscore. If the current space is the first one in the string, it simply appends an underscore. Otherwise, it appends the character to the result. The result is then returned as a string.