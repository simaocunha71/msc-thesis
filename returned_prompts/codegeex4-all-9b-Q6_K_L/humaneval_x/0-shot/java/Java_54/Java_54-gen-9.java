```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean sameChars(String s0, String s1) {
        if (s0.length() != s1.length()) {
            return false;
        }
        int[] count0 = new int[256];
        int[] count1 = new int[256];
        for (int i = 0; i < s0.length(); i++) {
            count0[s0.charAt(i)]++;
            count1[s1.charAt(i)]++;
        }
        for (int i = 0; i < 256; i++) {
            if (count0[i] != count1[i]) {
                return false;
            }
        }
        return true;
    }
}
```