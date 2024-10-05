Here is a Java solution that uses a HashMap to count the frequency of each character in both strings. It then compares these frequencies to determine if the strings have the same characters.

```java
import java.util.*;

class Solution {
    public boolean sameChars(String s0, String s1) {
        if (s0.length() != s1.length()) {
            return false;
        }

        Map<Character, Integer> map0 = new HashMap<>();
        Map<Character, Integer> map1 = new HashMap<>();

        for (char c : s0.toCharArray()) {
            map0.put(c, map0.getOrDefault(c, 0) + 1);
        }

        for (char c : s1.toCharArray()) {
            map1.put(c, map1.getOrDefault(c, 0) + 1);
        }

        return map0.equals(map1);
    }
}
```

This solution has a time complexity of O(n), where n is the length of the strings, because it needs to iterate over the characters in both strings once. The space complexity is also O(n), because in the worst case, it needs to store all characters in the maps.