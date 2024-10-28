Here is a simple Java solution for the problem:

```java
public String fixSpaces(String text) {
    StringBuilder sb = new StringBuilder();
    boolean spaceFound = false;
    for (char c : text.toCharArray()) {
        if (c == ' ') {
            if (!spaceFound) {
                sb.append(c);
                spaceFound = true;
            } else if (spaceFound) {
                sb.append('-');
                spaceFound = false;
            }
        } else {
            sb.append(c);
            spaceFound = false;
        }
    }
    return sb.toString();
}
```

This solution iterates over the input string character by character. If the character is a space, it checks if a space has been found before. If not, it simply appends the space to the result. If a space has been found before, it appends a hyphen to the result and resets the flag. If the character is not a space, it appends the character to the result and resets the flag. At the end, it returns the result as a string. 