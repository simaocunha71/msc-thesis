The task is to create a function that checks if the last character of a given string is an alphabetical character and it's not part of a word. A "word" is considered as a group of characters separated by a space.

Here's the solution in Java:

```java
public boolean checkIfLastCharIsALetter(String txt) {
    if (txt == null || txt.length() == 0) {
        return false;
    }
    char lastChar = txt.charAt(txt.length() - 1);
    if (!Character.isLetter(lastChar)) {
        return false;
    }
    for (int i = txt.length() - 2; i >= 0; i--) {
        if (Character.isWhitespace(txt.charAt(i))) {
            return true;
        }
    }
    return false;
}
```

This function first checks if the string is null or empty. If it is, the function returns false. Then it checks if the last character of the string is a letter. If it's not, the function returns false. After that, the function checks if the last character is part of a word by iterating from the second last character to the first character of the string and checking if any of them is a whitespace character. If it finds a whitespace character, it returns true, indicating that the last character is part of a word. If it doesn't find any whitespace character, it returns false, indicating that the last character is not part of a word. 