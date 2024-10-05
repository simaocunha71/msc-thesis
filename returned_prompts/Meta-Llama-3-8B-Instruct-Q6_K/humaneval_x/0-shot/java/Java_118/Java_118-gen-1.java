The problem can be solved by iterating through the word from right to left and checking if the character is a vowel or not. We keep track of the last consonant we encountered and the index of the last vowel. If we encounter a vowel and the last consonant is not null, we update the index of the closest vowel. If we encounter a consonant and the last consonant is not null, we update the last consonant. If the last consonant is null, it means we are at the beginning of the word, so we continue iterating. If we reach the end of the word and the last consonant is not null, it means we didn't find a vowel between two consonants, so we return an empty string.

Here is the Java code for the solution:

```java
public String getClosestVowel(String word) {
    char[] charArray = word.toCharArray();
    int lastConsonantIndex = -1;
    int closestVowelIndex = -1;
    for (int i = charArray.length - 1; i >= 0; i--) {
        char c = charArray[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            if (lastConsonantIndex != -1) {
                closestVowelIndex = i;
            }
        } else {
            lastConsonantIndex = i;
        }
    }
    return closestVowelIndex == -1 ? "" : String.valueOf(charArray[closestVowelIndex]);
}
```

This solution has a time complexity of O(n), where n is the length of the word, because we iterate through the word once. The space complexity is O(1), because we use a constant amount of space to store the last consonant index and the closest vowel index.