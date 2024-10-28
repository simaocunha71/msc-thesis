Here is a Java solution for the problem:

```java
public String getClosestVowel(String word) {
    for (int i = word.length() - 2; i > 0; i--) {
        char c = word.charAt(i);
        if (isVowel(c) && !isVowel(word.charAt(i - 1)) && !isVowel(word.charAt(i + 1))) {
            return String.valueOf(c);
        }
    }
    return "";
}

private boolean isVowel(char c) {
    return "AEIOUaeiou".indexOf(c) != -1;
}
```

This code works by iterating over the word from right to left, checking each character to see if it is a vowel and surrounded by consonants. The `isVowel` method checks if a character is a vowel by looking for it in a string of vowels.

In the `getClosestVowel` method, we start iterating from the second last character (`i = word.length() - 2`) and go until the second character (`i > 0`). We then check if the current character is a vowel and the characters before and after it are not vowels. If all these conditions are met, we return the current character. If we don't find any character that meets these conditions, we return an empty string.