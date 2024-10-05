```java
import java.util.*;
import java.lang.*;

class Solution {
    public String solve(int N) {
        String binary = Integer.toBinaryString(N);
        int sum = 0;
        for (int i = 0; i < binary.length(); i++) {
            if (binary.charAt(i) == '1') {
                sum++;
            }
        }
        return Integer.toBinaryString(sum);
    }
}
```