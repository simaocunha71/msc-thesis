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
    return "aeiouAEIOU".indexOf(c) != -1;
}

Explanation:
The problem is asking to write a function that takes a string as input and returns the same string but without any vowels. 

In the given solution, we use a StringBuilder to efficiently build the resulting string. We iterate over each character in the input string and check if it's a vowel using the `isVowel` function. If it's not a vowel, we append it to the StringBuilder. 

The `isVowel` function checks if a character is a vowel by searching for its index in the string "aeiouAEIOU". If the index is not -1, the character is a vowel. 

This solution has a time complexity of O(n), where n is the length of the input string, because we're iterating over each character once. The space complexity is O(n) as well, because we're using a StringBuilder to store the resulting string. 





```java
public class Solution {
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
        return "aeiouAEIOU".indexOf(c) != -1;
    }
}
```

This solution uses a StringBuilder to efficiently build the resulting string. It iterates over each character in the input string and checks if it's a vowel using the `isVowel` function. If it's not a vowel, it appends it to the StringBuilder. The `isVowel` function checks if a character is a vowel by searching for its index in the string "aeiouAEIOU". If the index is not -1, the character is a vowel. This solution has a time complexity of O(n), where n is the length of the input string, because we're iterating over each character once. The space complexity is O(n) as well, because we're using a StringBuilder to store the resulting string.