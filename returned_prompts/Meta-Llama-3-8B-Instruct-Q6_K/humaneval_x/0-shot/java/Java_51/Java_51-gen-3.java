Here is the solution in Java:

```java
public String removeVowels(String text) {
    String result = "";
    for (int i = 0; i < text.length(); i++) {
        char c = text.charAt(i);
        if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U') {
            result += c;
        }
    }
    return result;
}
```

This function iterates over each character in the input string. If the character is not a vowel (either lowercase or uppercase), it is added to the result string. At the end of the function, the result string is returned, which is the input string with all vowels removed. 

This function has a time complexity of O(n), where n is the length of the input string, because it makes one pass over the input string. The space complexity is also O(n), because in the worst case (when all characters are not vowels), the result string will have the same length as the input string. 

Please note that this function considers 'y' as a consonant, not a vowel. If you want to consider 'y' as a vowel, you can add 'y' and 'Y' to the list of vowels in the if condition. 