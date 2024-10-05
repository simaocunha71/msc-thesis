```java
import java.util.*;
import java.lang.*;

class Solution {
    public String stringXor(String a, String b) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) == b.charAt(i)) {
                result.append('0');
            } else {
                result.append('1');
            }
        }

        return result.toString();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.stringXor("010", "110")); // "100"
    }
}
```