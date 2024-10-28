```java
import java.util.*;
import java.lang.*;

class Solution {
    public String solve(int N) {
        String bin = Integer.toBinaryString(N);
        int sum = 0;
        for (char c : bin.toCharArray()) {
            sum += c - '0';
        }
        return Integer.toBinaryString(sum);
    }
}
```