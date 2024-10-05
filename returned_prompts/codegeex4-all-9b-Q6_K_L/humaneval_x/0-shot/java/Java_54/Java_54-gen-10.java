```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean sameChars(String s0, String s1) {
        // If the lengths of the strings are not equal, they cannot have the same characters
        if (s0.length() != s1.length()) {
            return false;
        }

        // Create a frequency map for the characters in the first string
        Map<Character, Integer> freqMap = new HashMap<>();
        for (char c : s0.toCharArray()) {
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }

        // Check the frequency of each character in the second string
        for (char c : s1.toCharArray()) {
            // If the character is not in the frequency map or its count is zero, the strings do not have the same characters
            if (!freqMap.containsKey(c) || freqMap.get(c) == 0) {
                return false;
            }
            // Decrease the count of the character in the frequency map
            freqMap.put(c, freqMap.get(c) - 1);
        }

        return true;
    }
}
```