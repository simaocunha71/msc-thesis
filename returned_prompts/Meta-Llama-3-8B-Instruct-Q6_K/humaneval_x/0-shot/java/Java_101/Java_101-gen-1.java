```java
import java.util.*;

class Solution {
    public List<String> wordStrings(String s) {
        List<String> result = new ArrayList<>();
        String[] words = s.split("[,\\s]+");
        for (String word : words) {
            if (!word.isEmpty()) {
                result.add(word.trim());
            }
        }
        return result;
    }
}
```

Explanation:
The problem is to split a given string into words and return a list of those words. The string can contain commas or spaces as separators.

Here's the solution:

1. We use the `split()` method to split the input string into an array of words. The regular expression `[\\s,]+` matches one or more occurrences of either a comma or a space.
2. We iterate through the array of words and add each non-empty word to the result list. We use the `trim()` method to remove any leading or trailing whitespace from each word.
3. Finally, we return the result list.

Note that the `split()` method returns an array of strings, and we use an enhanced for loop to iterate through the array. We also use the `trim()` method to remove any leading or trailing whitespace from each word. This ensures that the resulting list of words is clean and free of unnecessary whitespace.