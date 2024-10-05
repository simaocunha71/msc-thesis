Here is a Java solution using a for loop to iterate through the string in reverse order. If the current character is a vowel and the previous and next characters are consonants, it returns the current vowel. If no such vowel is found, it returns an empty string.

```java
public String getClosestVowel(String word) {
    String vowels = "aeiouAEIOU";
    for (int i = word.length() - 1; i >= 1; i--) {
        char current = word.charAt(i);
        if (vowels.indexOf(current) != -1) {
            char prev = word.charAt(i - 1);
            char next = word.charAt(i + 1);
            if (vowels.indexOf(prev) == -1 && vowels.indexOf(next) == -1) {
                return String.valueOf(current);
            }
        }
    }
    return "";
}
```
The time complexity of this solution is O(n), where n is the length of the string. The space complexity is O(1), as it only uses a few extra variables.