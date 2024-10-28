```java
import java.util.*;

public class Solution {
    public String antiShuffle(String s) {
        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();
        
        for(String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            result.append(new String(chars)).append(" ");
        }
        
        return result.toString().trim();
    }
}
```

Explanation:
1. We split the input string into individual words using the `split` method with a space character as the delimiter.
2. We iterate through each word and convert it to a character array using the `toCharArray` method.
3. We sort the character array in ascending order using the `Arrays.sort` method.
4. We create a new string from the sorted character array using the `String` constructor.
5. We append the sorted string to a `StringBuilder` object, followed by a space character.
6. Finally, we return the `StringBuilder` object as a string, and use the `trim` method to remove any trailing spaces.

Note: The `trim` method is used to remove any trailing spaces from the resulting string. If you don't want to remove trailing spaces, you can remove the `trim` method call.