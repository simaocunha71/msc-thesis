Here's how you can write this function in Java:

```java
public String flipCase(String string) {
    StringBuilder sb = new StringBuilder(string);
    for (int i = 0; i < sb.length(); i++) {
        char c = sb.charAt(i);
        if (Character.isLowerCase(c)) {
            sb.setCharAt(i, Character.toUpperCase(c));
        } else if (Character.isUpperCase(c)) {
            sb.setCharAt(i, Character.toLowerCase(c));
        }
    }
    return sb.toString();
}
```

This function uses a `StringBuilder` to iterate over the characters of the string. For each character, it checks if it is lowercase or uppercase using the `Character.isLowerCase()` and `Character.isUpperCase()` methods. If the character is lowercase, it converts it to uppercase using `Character.toUpperCase()`. If the character is uppercase, it converts it to lowercase using `Character.toLowerCase()`. Finally, it returns the modified string.

In your example, it would return `"hELLO"` for the input `"Hello"`.