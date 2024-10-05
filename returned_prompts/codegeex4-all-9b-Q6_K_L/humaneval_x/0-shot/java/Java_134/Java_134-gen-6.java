Here is the Java code:

```java
public boolean checkIfLastCharIsALetter(String txt) {
    if (txt == null || txt.isEmpty()) {
        return false;
    }
    char lastChar = txt.charAt(txt.length() - 1);
    return Character.isLetter(lastChar) && !txt.matches(".*\\b.*" + lastChar + ".*\\b.*");
}
```

This function first checks if the input string is null or empty. If it is, it returns false.

Then it gets the last character of the string and checks if it is a letter.

The regular expression `.*\\b.*` checks if the character is not a part of a word. If the character is a part of a word, the regular expression matches the string. Otherwise, it doesn't match the string.

If the last character is a letter and is not a part of a word, the function returns true. Otherwise, it returns false.