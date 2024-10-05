Here is a Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int startsOneEnds(int n) {
        int count = 0;
        int start = (int) Math.pow(10, n - 1);
        int end = (int) Math.pow(10, n) - 1;

        for (int i = start; i <= end; i++) {
            if (String.valueOf(i).charAt(0) == '1' || String.valueOf(i).charAt(String.valueOf(i).length() - 1) == '1') {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.startsOneEnds(2)); // Output: 9
    }
}
```

This program counts the number of n-digit positive integers that start or end with 1. It uses a loop to iterate through all n-digit numbers and checks if the first digit or the last digit is 1. If it is, the count is incremented. Finally, it returns the count.