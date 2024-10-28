Here is a Java function that fulfills the requirements:

```java
public boolean checkIfLastCharIsALetter(String txt) {
    if (txt.isEmpty()) {
        return false;
    }

    char lastChar = txt.charAt(txt.length() - 1);
    if (!Character.isLetter(lastChar)) {
        return false;
    }

    String[] words = txt.split(" ");
    for (String word : words) {
        if (word.length() > 0 && word.charAt(word.length() - 1) == lastChar) {
            return false;
        }
    }

    return true;
}
```

This function first checks if the input string is empty. If it is, the function returns false. Then it checks if the last character of the string is a letter. If it is not, the function returns false. If the last character is a letter, the function splits the string into words and checks if any of the words end with the last character. If any of them do, the function returns false. If none of the words end with the last character, the function returns true. 