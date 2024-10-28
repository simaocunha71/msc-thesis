```java
public String fixSpaces(String text) {
    StringBuilder sb = new StringBuilder();
    int count = 0;
    for (int i = 0; i < text.length(); i++) {
        if (text.charAt(i) == ' ') {
            if (count == 0) {
                sb.append('_');
                count++;
            } else if (count == 1) {
                sb.append('_');
                count++;
            } else {
                sb.append('-');
                count = 0;
            }
        } else {
            sb.append(text.charAt(i));
            count = 0;
        }
    }
    return sb.toString();
}
```
Explanation:
This problem can be solved by iterating through the input string and replacing spaces with underscores and handling consecutive spaces. A StringBuilder is used to efficiently build the output string.

In the loop, we check if the current character is a space. If it is, we increment the count of consecutive spaces. If the count is 0, we append an underscore to the StringBuilder. If the count is 1, we also append an underscore. If the count is 2 or more, we append a hyphen and reset the count to 0. If the current character is not a space, we append it to the StringBuilder and reset the count to 0.

Finally, we return the StringBuilder as a string. This solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n) for the StringBuilder.