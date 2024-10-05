The problem asks to create a function that checks if the last character of a given string is an alphabetical character and is not part of a word. A "word" is considered as a group of characters separated by spaces. The function should return true if the condition is met and false otherwise.

Here is the Java solution for the problem:

```java
public boolean checkIfLastCharIsALetter(String txt) {
    if(txt.length() == 0) return false; // If the string is empty, return false
    String[] words = txt.split(" "); // Split the string into words
    String lastWord = words[words.length - 1]; // Get the last word
    if(lastWord.length() == 0) return false; // If the last word is empty, return false
    char lastChar = lastWord.charAt(lastWord.length() - 1); // Get the last character of the last word
    return Character.isLetter(lastChar) && !lastWord.endsWith(String.valueOf(lastChar)); // Check if the last character is a letter and not part of a word
}
```

In this solution, we first split the string into words using the `split` method. Then, we get the last word and check if it's empty. If it's not empty, we get the last character of the last word. We then use the `Character.isLetter` method to check if the last character is a letter. Finally, we use the `endsWith` method to check if the last character is not part of a word. If both conditions are met, we return true; otherwise, we return false. 