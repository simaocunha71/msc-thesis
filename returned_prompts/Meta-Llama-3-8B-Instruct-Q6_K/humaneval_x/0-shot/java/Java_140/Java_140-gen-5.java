```java
public String fixSpaces(String text) {
    StringBuilder sb = new StringBuilder();
    boolean space = false;
    for (char c : text.toCharArray()) {
        if (c == ' ') {
            if (space) {
                sb.append('-');
                space = false;
            } else {
                sb.append('_');
                space = true;
            }
        } else {
            sb.append(c);
            space = false;
        }
    }
    return sb.toString();
}
```
Explanation:
The function `fixSpaces` takes a string `text` as input and returns a new string with all spaces replaced with underscores and consecutive spaces replaced with -. The function uses a `StringBuilder` to build the new string.

It iterates over each character `c` in the input string `text`. If `c` is a space, it checks if the previous character was also a space. If it was, it appends - to the `StringBuilder`, otherwise it appends _. If `c` is not a space, it simply appends `c` to the `StringBuilder` and resets the `space` flag.

Finally, the function returns the `StringBuilder` as a string.

This solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n), as it uses a `StringBuilder` to store the result.