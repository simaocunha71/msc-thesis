```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean sameChars(String s0, String s1) {
        // Check if the lengths of the two strings are equal
        if (s0.length() != s1.length()) {
            return false;
        }
        
        // Convert the strings to character arrays
        char[] arr0 = s0.toCharArray();
        char[] arr1 = s1.toCharArray();
        
        // Sort the character arrays
        Arrays.sort(arr0);
        Arrays.sort(arr1);
        
        // Compare the sorted arrays
        return Arrays.equals(arr0, arr1);
    }
}
```