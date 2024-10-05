```java
public String removeVowels(String text) {
    StringBuilder result = new StringBuilder();
    for (char c : text.toCharArray()) {
        if (!isVowel(c)) {
            result.append(c);
        }
    }
    return result.toString();
}

private boolean isVowel(char c) {
    return "aeiouAEIOU".indexOf(c) != -1;
}
```

Explanation:
The function `removeVowels` takes a string as input and returns a new string without any vowels. It iterates over each character in the input string and checks if the character is a vowel using the `isVowel` function. If the character is not a vowel, it is appended to the `result` string. Finally, the function returns the `result` string.

The `isVowel` function checks if a character is a vowel by checking if the character is present in the string "aeiouAEIOU". If the character is found, the function returns `true`, indicating that the character is a vowel. Otherwise, it returns `false`. This function is used in the `removeVowels` function to filter out vowels from the input string.