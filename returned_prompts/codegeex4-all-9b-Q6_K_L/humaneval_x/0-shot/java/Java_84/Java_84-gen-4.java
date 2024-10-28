```java
import java.util.*;
import java.lang.*;

class Solution {
    public String solve(int N) {
        // Initialize a variable to store the sum of digits
        int sum = 0;

        // Convert the integer to a string to iterate through each digit
        String str = Integer.toString(N);

        // Iterate through each digit and add it to the sum
        for (char c : str.toCharArray()) {
            sum += Character.getNumericValue(c);
        }

        // Convert the sum to a binary string
        String binary = Integer.toBinaryString(sum);

        // Return the binary string
        return binary;
    }
}
```