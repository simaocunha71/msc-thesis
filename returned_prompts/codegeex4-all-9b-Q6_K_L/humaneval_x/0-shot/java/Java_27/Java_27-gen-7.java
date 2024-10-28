```java
public String flipCase(String string) {
    String result = "";
    for (int i = 0; i < string.length(); i++) {
        char c = string.charAt(i);
        if (Character.isLowerCase(c)) {
            result += Character.toUpperCase(c);
        } else if (Character.isUpperCase(c)) {
            result += Character.toLowerCase(c);
        } else {
            result += c;
        }
    }
    return result;
}
```