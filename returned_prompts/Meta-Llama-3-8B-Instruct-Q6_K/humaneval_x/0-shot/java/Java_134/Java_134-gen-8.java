Here is the Java solution for the problem:

```java
public boolean checkIfLastCharIsALetter(String txt) {
    if (txt == null || txt.isEmpty()) {
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

In this solution, we first check if the given string is null or empty. If it is, we return false. Then, we split the string into words using the split function. We check if the last word is empty. If it is, we return false. Finally, we get the last character of the last word and check if it's a letter using the Character.isLetter function. If it is, we return true; otherwise, we return false. 