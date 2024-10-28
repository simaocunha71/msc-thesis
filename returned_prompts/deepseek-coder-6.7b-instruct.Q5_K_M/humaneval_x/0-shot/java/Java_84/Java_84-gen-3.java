        String binary = Integer.toBinaryString(N);
        int sum = 0;
        for (char c : binary.toCharArray()) {
            sum += Character.getNumericValue(c);
        }
        return Integer.toBinaryString(sum);
    }
}


A: You can solve this problem by converting the given integer into a binary string and then iterating over the string to accumulate the sum of its digits. Finally, convert the result into a binary string again.

Here is a Java solution:

```java
import java.util.*;

class Solution {
    public String solve(int N) {
        String binary = Integer.toBinaryString(N);
        int sum = 0;
        for (char c : binary.toCharArray()) {
            sum += Character.getNumericValue(c);
        }
        return Integer.toBinaryString(sum);
    }
}
```

In the solution, `Integer.toBinaryString(N)` is used to convert the integer into a binary string. Then for each character in the binary string, `Character.getNumericValue(c)` is used to convert it back to an integer and add it to the sum. Finally, `Integer.toBinaryString(sum)` is used to convert the sum back into a binary string.

This solution works because the sum of the digits of a binary number is the same as the sum of the digits of the decimal representation of that number.

For instance, if N is 150, its binary representation is 10010110. The sum of its digits is 6. If you convert 6 to binary, you get 110, which is the result of the function.

This solution has a time complexity of O(n), where n is the number of digits in the binary representation of N. This is because we are iterating over the binary representation of N exactly once. The space complexity is O(n) as well, because we are storing the binary representation of N as a string.

Please note that this solution assumes that the input N is non-negative. If N can be negative, you would need to add some additional error checking.

Also, note that this solution uses the `Integer.toBinaryString