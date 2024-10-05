Here is the solution:
```java
import java.util.*;

class Solution {
    public boolean sameChars(String s0, String s1) {
        if (s0.length() != s1.length()) {
            return false;
        }

        Map<Character, Integer> map0 = new HashMap<>();
        Map<Character, Integer> map1 = new HashMap<>();

        for (int i = 0; i < s0.length(); i++) {
            char c0 = s0.charAt(i);
            char c1 = s1.charAt(i);

            map0.put(c0, map0.getOrDefault(c0, 0) + 1);
            map1.put(c1, map1.getOrDefault(c1, 0) + 1);
        }

        return map0.equals(map1);
    }
}
```
Explanation:

1. Check if the two strings have the same length. If not, return `false`.
2. Create two HashMaps, `map0` and `map1`, to store the characters and their frequencies in the two strings.
3. Iterate through the characters of the two strings. For each character, increment the count in the corresponding HashMap.
4. Compare the two HashMaps using the `equals` method. If they are equal, it means the two strings have the same characters, so return `true`. Otherwise, return `false`.