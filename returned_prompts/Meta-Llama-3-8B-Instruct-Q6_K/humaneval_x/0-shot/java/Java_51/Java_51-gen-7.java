Here is the solution to the problem:

```java
import java.util.*;

class Solution {
    public String removeVowels(String text) {
        String vowels = "aeiouAEIOU";
        StringBuilder result = new StringBuilder();
        
        for(int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);
            if (!vowels.indexOf(ch) != -1) {
                result.append(ch);
            }
        }
        
        return result.toString();
    }
}
```


This function iterates over each character in the input string. If the character is not a vowel (i.e., not in the string "aeiouAEIOU"), it is added to the result string. The result is then returned as a string. This solution has a time complexity of O(n), where n is the length of the input string, because it iterates over each character in the string once. It also uses a constant amount of space, so its space complexity is O(1). 