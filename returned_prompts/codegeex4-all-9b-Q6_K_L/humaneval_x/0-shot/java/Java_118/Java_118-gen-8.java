Here is a possible solution in Java:

```java
public String getClosestVowel(String word) {
    if (word.length() < 3) {
        return "";
    }
    for (int i = word.length() - 3; i >= 0; i--) {
        if (isConsonant(word.charAt(i + 1)) && isConsonant(word.charAt(i + 2)) && isVowel(word.charAt(i))) {
            return String.valueOf(word.charAt(i));
        }
    }
    return "";
}

private boolean isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
           c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
}

private boolean isConsonant(char c) {
    return c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z' && !isVowel(c);
}
```

Explanation:
- The `getClosestVowel` function checks if the length of the word is less than 3. If so, it returns an empty string.
- Then it iterates from the end of the word to the beginning, checking if the current character is a vowel and the next two characters are consonants.
- If a vowel is found, it returns the vowel as a string.
- If no vowel is found, it returns an empty string.
- The `isVowel` function checks if a character is a vowel.
- The `isConsonant` function checks if a character is a consonant.