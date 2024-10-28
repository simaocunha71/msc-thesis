```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean sameChars(String s0, String s1) {
        if (s0.length() != s1.length()) {
            return false;
        }
        char[] arr0 = s0.toCharArray();
        char[] arr1 = s1.toCharArray();
        Arrays.sort(arr0);
        Arrays.sort(arr1);
        return Arrays.equals(arr0, arr1);
    }
}
```