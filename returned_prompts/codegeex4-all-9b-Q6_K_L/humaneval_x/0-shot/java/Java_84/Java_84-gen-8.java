```java
import java.util.*;
import java.lang.*;

class Solution {
    public String solve(int N) {
        String binary = Integer.toBinaryString(N);
        int sum = 0;
        for (char c : binary.toCharArray()) {
            if (c == '1') {
                sum++;
            }
        }
        return Integer.toBinaryString(sum);
    }
}
```