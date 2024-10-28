```java
public String removeVowels(String text) {
    String result = "";
    for(int i = 0; i < text.length(); i++) {
        char c = text.charAt(i);
        if(c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U') {
            result += c;
        }
    }
    return result;
}
```
Explanation:
This function iterates over each character in the input string. If the character is not a vowel (either lowercase or uppercase), it is added to the result string. At the end, the function returns the result string, which is the original string with all vowels removed.

For example, if the input is "abcdef", the function will return "bcdf" because 'a', 'e', and 'f' are vowels and are removed. If the input is "zbcd", the function will return "zbcd" because there are no vowels to remove. If the input is "aaaaa", the function will return an empty string because all characters are vowels and are removed. 