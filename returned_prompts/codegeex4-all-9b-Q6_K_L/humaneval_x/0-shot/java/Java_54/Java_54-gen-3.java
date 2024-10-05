```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean sameChars(String s0, String s1) {
        if (s0.length() != s1.length()) return false;
        Map<Character, Integer> countMap = new HashMap<>();
        for (char c : s0.toCharArray()) {
            countMap.put(c, countMap.getOrDefault(c, 0) + 1);
        }
        for (char c : s1.toCharArray()) {
            if (!countMap.containsKey(c) || countMap.get(c) == 0) return false;
            countMap.put(c, countMap.get(c) - 1);
        }
        return true;
    }
}
```