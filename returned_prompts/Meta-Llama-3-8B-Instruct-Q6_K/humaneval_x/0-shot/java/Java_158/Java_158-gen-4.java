Here is the Java code for the problem:

```java
import java.util.*;

class Solution {
    public String findMax(List<String> words) {
        String result = "";
        int maxCount = 0;
        for (String word : words) {
            Set<Character> set = new HashSet<>();
            for (char c : word.toCharArray()) {
                set.add(c);
            }
            if (set.size() > maxCount) {
                maxCount = set.size();
                result = word;
            } else if (set.size() == maxCount) {
                if (result.compareTo(word) > 0) {
                    result = word;
                }
            }
        }
        return result;
    }
}
```

In this solution, we iterate over the list of words and for each word, we create a set of unique characters. We then compare the size of the set with the maximum count. If the size is greater, we update the maximum count and the result word. If the size is equal, we compare the words lexicographically and update the result word if the current word is smaller. Finally, we return the result word. If the list is empty, the function returns an empty string.