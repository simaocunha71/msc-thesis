```java
public String flipCase(String string) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < string.length(); i++) {
        char c = string.charAt(i);
        if (Character.isUpperCase(c)) {
            sb.append(Character.toLowerCase(c));
        } else if (Character.isLowerCase(c)) {
            sb.append(Character.toUpperCase(c));
        } else {
            sb.append(c);
        }
    }
    return sb.toString();
}
```