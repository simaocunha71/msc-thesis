To solve this problem, you need to iterate through the string from right to left and check for the closest vowel that stands between two consonants. Here's a possible solution:

```java
public String getClosestVowel(String word) {
    String vowels = "aeiouAEIOU";
    int length = word.length();
    for (int i = length - 2; i >= 1; i--) {
        char currentChar = word.charAt(i);
        char previousChar = word.charAt(i - 1);
        char nextChar = word.charAt(i + 1);
        if (vowels.contains(String.valueOf(currentChar)) && !vowels.contains(String.valueOf(previousChar)) && !vowels.contains(String.valueOf(nextChar))) {
            return String.valueOf(currentChar);
        }
    }
    return "";
}
```

In this solution, we start iterating from the third-to-last character in the string and go all the way to the second character. For each character, we check if it is a vowel and the previous and next characters are not vowels. If all these conditions are met, we return the vowel character. If no such vowel is found, we return an empty string.