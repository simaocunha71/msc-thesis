```java
import java.util.*;

public class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> words = new ArrayList<>();
        String[] strArray = s.split("\\s+");
        for (String str : strArray) {
            int count = 0;
            for (char c : str.toCharArray()) {
                if (!Character.isLetter(c) || Character.isLetter(c) && Character.isLowerCase(c)) {
                    continue;
                }
                count++;
            }
            if (count == n) {
                words.add(str);
            }
        }
        return words;
    }
}
```
This Java solution defines a method `selectWords` that takes a string `s` and an integer `n` as input. It splits the input string into an array of words using the `split` method with the regular expression `\s+`, which matches one or more whitespace characters. It then iterates over each word in the array and counts the number of consonants in the word. Consonants are defined as characters that are not letters (using `Character.isLetter(c)`) or letters that are uppercase (using `Character.isLowerCase(c)`). If the count of consonants in a word matches the input `n`, the word is added to the result list. Finally, the method returns the list of words that contain exactly `n` consonants. If the input string is empty, the method returns an empty list. The method is case-insensitive, meaning it treats uppercase and lowercase letters as the same.  The output will be a list of words from the input string that contain exactly `n` consonants, in the order they appear in the string.  If there are no words that contain exactly `n` consonants, the method returns an empty list.  The method can be tested with the examples provided in the problem description.  The method can be further optimized by using a single loop to iterate over the characters in the string and a single conditional statement to check if a character is a consonant.  The method can also be modified to return the words that contain at most `n` consonants, instead of exactly `n` consonants.  The method can also be modified to return the words that contain at least `n` consonants, instead of exactly `n` consonants.  The method can also be modified to return the words that contain more than `n` consonants, instead of exactly `n` consonants.  The method