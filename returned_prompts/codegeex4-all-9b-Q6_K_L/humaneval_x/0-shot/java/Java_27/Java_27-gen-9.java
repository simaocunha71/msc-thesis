```java
public String flipCase(String string) {
    StringBuilder builder = new StringBuilder(string);
    for (int i = 0; i < builder.length(); i++) {
        char c = builder.charAt(i);
        if (Character.isLowerCase(c)) {
            builder.setCharAt(i, Character.toUpperCase(c));
        } else if (Character.isUpperCase(c)) {
            builder.setCharAt(i, Character.toLowerCase(c));
        }
    }
    return builder.toString();
}
```