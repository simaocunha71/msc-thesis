Here is the Java code for the problem:

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
        return String.valueOf(sum);
    }
}
```

The `solve` method takes an integer `N` as input and converts it to binary using the `Integer.toBinaryString` method. It then iterates over each character in the binary string and increments a sum variable if the character is '1'. Finally, it returns the sum as a string using the `String.valueOf` method.

This solution is efficient and works within the constraints provided.