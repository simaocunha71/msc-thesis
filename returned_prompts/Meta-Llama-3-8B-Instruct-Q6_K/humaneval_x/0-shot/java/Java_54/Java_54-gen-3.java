Here is a Java solution for the problem:

```java
import java.util.*;

public class Solution {
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

This solution first checks if the two strings have the same length. If they don't, it returns false because they cannot have the same characters. Then it creates two maps, one for each string, where the keys are the characters and the values are the counts of these characters. Finally, it checks if the two maps are equal. If they are, it returns true; otherwise, it returns false.

This solution has a time complexity of O(n), where n is the length of the strings, because it needs to iterate over each character in the strings once. The space complexity is also O(n), because in the worst case, all characters in the strings are unique, so the maps will contain n entries. 