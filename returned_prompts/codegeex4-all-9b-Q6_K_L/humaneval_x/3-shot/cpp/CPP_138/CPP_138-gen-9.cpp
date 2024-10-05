Here is a simple Java program that solves the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    countUpper("aBCdEf") returns 1
    countUpper("abcdefg") returns 0
    countUpper("dBBE") returns 0
     */    
    public int countUpper(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i += 2) {
            char c = s.charAt(i);
            if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                count++;
            }
        }
        return count;
    }
}
```

The `countUpper` function iterates over the characters in the string `s`, checking if they are an uppercase vowel. If they are, it increments the `count` variable. The function then returns the `count` variable as the result.

This function works by iterating over the characters in the string `s`, starting at index 0 and incrementing by 2 each time. This means that it checks every other character in the string, which corresponds to even indices in the original string.