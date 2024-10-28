Here is a Java solution to the problem:

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
            map0.put(s0.charAt(i), map0.getOrDefault(s0.charAt(i), 0) + 1);
            map1.put(s1.charAt(i), map1.getOrDefault(s1.charAt(i), 0) + 1);
        }

        return map0.equals(map1);
    }
}
```

This solution works by first checking if the two strings have the same length. If they don't, it immediately returns false, because two strings with different lengths cannot have the same characters.

Then, it creates two hash maps, one for each string, where the keys are the characters in the string and the values are the counts of each character. It then iterates over the characters in the strings, incrementing the count for each character in the hash map.

Finally, it compares the two hash maps using the equals method. If the hash maps are equal, it means that the two strings have the same characters, and it returns true. Otherwise, it returns false.