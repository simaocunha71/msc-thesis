Here is the Java solution for the problem. The function `removeVowels` iterates over each character in the input string and checks if the character is a vowel. If it is not a vowel, it is added to the result string. The vowels are defined as 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'. 

```java
import java.util.*;

class Solution {
    public String removeVowels(String text) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U') {
                result.append(c);
            }
        }
        return result.toString();
    }
}
```


The time complexity of this solution is O(n), where n is the length of the input string. This is because we are iterating over each character in the string once. The space complexity is also O(n), as in the worst case, the result string could be the same length as the input string. 

This solution assumes that the input string only contains ASCII characters. If the input string can contain non-ASCII characters, you would need to adjust the solution accordingly. 

The `StringBuilder` class is used to efficiently build the result string. The `charAt` method is used to get the character at a specific index in the input string. The `append` method is used to add a character to the result string. The `toString` method is used to convert the `StringBuilder` object to a string. 












