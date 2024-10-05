The problem is asking whether two given strings have the same characters, regardless of their order and frequency. We can solve this problem by sorting the characters in both strings and comparing the results.

Here is the Java solution:

```java
import java.util.*;

public class Solution {
    public boolean sameChars(String s0, String s1) {
        if (s0.length() != s1.length()) {
            return false;
        }

        String s0Sorted = sort(s0);
        String s1Sorted = sort(s1);

        return s0Sorted.equals(s1Sorted);
    }

    private String sort(String s) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }
}
```

In this solution, the `sameChars` method first checks if the lengths of the two strings are equal. If they are not, it returns `false` because the strings cannot have the same characters. If the lengths are equal, it sorts the characters in both strings and compares the results. If the sorted strings are equal, it returns `true`; otherwise, it returns `false`. The `sort` method is a helper method that sorts a string by converting it to a character array, sorting the array using the `Arrays.sort` method, and then converting the array back to a string. 