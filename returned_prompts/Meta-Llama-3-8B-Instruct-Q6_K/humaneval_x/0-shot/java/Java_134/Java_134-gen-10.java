Here is a Java solution for the problem:

```java
public boolean checkIfLastCharIsALetter(String txt) {
    if (txt.isEmpty()) {
        return false;
    }
    String[] words = txt.split(" ");
    if (words[words.length - 1].isEmpty()) {
        return false;
    }
    char lastChar = words[words.length - 1].charAt(words[words.length - 1].length() - 1);
    return Character.isLetter(lastChar);
}
```

This solution first checks if the input string is empty. If it is, it returns false. Then, it splits the string into an array of words using the `split` method. It checks if the last word is empty. If it is, it returns false. Finally, it checks if the last character of the last word is a letter using the `isLetter` method of the `Character` class. If it is, it returns true; otherwise, it returns false.