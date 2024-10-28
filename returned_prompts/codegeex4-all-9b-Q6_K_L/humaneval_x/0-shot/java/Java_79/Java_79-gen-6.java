To solve this problem, you need to convert the given decimal number to binary. In Java, you can use the Integer.toBinaryString() method to achieve this. However, the problem statement specifies that the binary number should be represented by a string with each character being '0' or '1', and the string should have extra characters 'db' at the beginning and at the end.

Here's the solution:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String decimalToBinary(int decimal) {
        return "db" + Integer.toBinaryString(decimal) + "db";
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.decimalToBinary(15));   // outputs "db1111db"
        System.out.println(solution.decimalToBinary(32));   // outputs "db100000db"
    }
}
```

In the solution, we use the Integer.toBinaryString() method to convert the decimal number to binary and then concatenate the extra characters 'db' at the beginning and at the end of the string.

The main() method is provided to test the solution.