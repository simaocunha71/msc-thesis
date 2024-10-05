```java
import java.util.*;
import java.lang.*;

class Solution {
    public String solve(int N) {
        String binaryString = Integer.toBinaryString(N);
        int sum = 0;
        for (char c : binaryString.toCharArray()) {
            sum += Character.getNumericValue(c);
        }
        return Integer.toString(sum);
    }
}
```