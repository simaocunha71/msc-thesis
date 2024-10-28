```java
public String removeVowels(String text) {
    StringBuilder sb = new StringBuilder();
    for (char c : text.toCharArray()) {
        if (!isVowel(c)) {
            sb.append(c);
        }
    }
    return sb.toString();
}

private boolean isVowel(char c) {
    c = Character.toLowerCase(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}
```


Explanation:
The problem is asking to create a function that takes a string as an input and returns the string without any vowels. The function should be case-insensitive, meaning it should treat 'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', and 'U' as vowels.

The solution uses a StringBuilder to construct the resulting string. It iterates over each character in the input string using a for-each loop. For each character, it checks if the character is a vowel using the isVowel function. If the character is not a vowel, it appends the character to the StringBuilder. Finally, it returns the StringBuilder as a string.

The isVowel function takes a character as an input and checks if it is a vowel. It converts the character to lowercase using the Character.toLowerCase method to make the function case-insensitive. It then checks if the character is one of the vowels 'a', 'e', 'i', 'o', or 'u'. If the character is a vowel, the function returns true; otherwise, it returns false.