```java
public String encrypt(String s) {
    if (s == null || s.length() == 0) {
        return "";
    }
    char[] result = new char[s.length()];
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (c >= 'a' && c <= 'z') {
            result[i] = (char) ((c - 'a' + 26 * 2) % 26 + 'a');
        } else if (c >= 'A' && c <= 'Z') {
            result[i] = (char) ((c - 'A' + 26 * 2) % 26 + 'A');
        } else {
            result[i] = c;
        }
    }
    return new String(result);
}
```