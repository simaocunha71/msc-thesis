To solve this problem, we can iterate through the string from right to left and check each character. We need to find a vowel that is surrounded by consonants from the right side of the word. Once we find such a vowel, we return it. If we don't find any such vowel, we return an empty string.

Here is the Java code to solve this problem:

```java
public String getClosestVowel(String word) {
    // Create a set of vowels
    Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));

    // Iterate through the string from right to left
    for (int i = word.length() - 1; i >= 0; i--) {
        char c = word.charAt(i);

        // Check if the character is a vowel
        if (vowels.contains(c)) {
            // Check if the character is surrounded by consonants from the right side
            if (i > 0 && i < word.length() - 1 && !vowels.contains(word.charAt(i - 1)) && !vowels.contains(word.charAt(i + 1))) {
                return String.valueOf(c);
            }
        }
    }

    // If no vowel is found, return an empty string
    return "";
}
```

This code will return the closest vowel that is surrounded by consonants from the right side of the word. If no such vowel is found, it will return an empty string.