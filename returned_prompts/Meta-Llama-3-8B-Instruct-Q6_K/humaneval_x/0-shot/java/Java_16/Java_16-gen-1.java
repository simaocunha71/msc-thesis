```java
import java.util.*;

class Solution {
    public int countDistinctCharacters(String string) {
        string = string.toLowerCase();
        Set<Character> set = new HashSet<>();
        for (char c : string.toCharArray()) {
            set.add(c);
        }
        return set.size();
    }
}
```


Here is the explanation:

1. We convert the string to lowercase using the `toLowerCase()` method to ignore case sensitivity.
2. We create a `HashSet` to store the distinct characters.
3. We iterate over the characters of the string using a `for` loop and add each character to the `HashSet`.
4. The `HashSet` automatically removes duplicates, so we can get the size of the `HashSet` to get the number of distinct characters.
5. We return the size of the `HashSet`.

This solution has a time complexity of O(n), where n is the length of the string, because we are iterating over the characters of the string once. The space complexity is also O(n), because in the worst case, all characters in the string are distinct and we need to store all of them in the `HashSet`.