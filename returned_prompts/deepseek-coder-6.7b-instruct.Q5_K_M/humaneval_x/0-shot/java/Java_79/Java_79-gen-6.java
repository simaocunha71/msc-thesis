        // Write your code here.
        return "db" + Integer.toBinaryString(decimal) + "db";
    }
}


A: Here is the solution using recursion:

```java
public class Solution {
    public String decimalToBinary(int n) {
        if (n == 0) {
            return "0";
        }
        if (n == 1) {
            return "1";
        }
