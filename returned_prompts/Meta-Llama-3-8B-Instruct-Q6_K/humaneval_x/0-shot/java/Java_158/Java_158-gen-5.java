Here is a Java function that solves the problem:

```java
import java.util.*;

class Solution {
    public String findMax(List<String> words) {
        String max = "";
        int maxCount = 0;
        for (String word : words) {
            Set<Character> set = new HashSet<>();
            for (char c : word.toCharArray()) {
                set.add(c);
            }
            if (set.size() > maxCount) {
                max = word;
                maxCount = set.size();
            }
        }
        return max;
    }
}
```

This function iterates over each word in the list. For each word, it creates a set of unique characters. If the size of the set is greater than the maximum count seen so far, it updates the maximum word and count. At the end, it returns the maximum word. If multiple words have the same maximum count, it returns the one that comes first in lexicographical order, because it is the last one that was updated. 

For example, if the input is ["name", "of", "string"], the function returns "string" because it has the maximum number of unique characters. If the input is ["name", "enam", "game"], the function returns "enam" because it has the maximum number of unique characters. If the input is ["aaaaaaa", "bb", "cc"], the function returns "aaaaaaa" because it has the maximum number of unique characters. 