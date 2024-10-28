        for (int i = n-1; i > 0; i--) {
            if (n % i == 0) {
                return i;
            }
        }
        return -1; // should never reach here
    }
}

The solution is straightforward, it starts from n-1 and goes down to 1, checking for every number if it is a divisor of n. The first found divisor is returned. If no divisor is found, -1 is returned.

It is worth noting that this solution is not very efficient, as its time complexity is O(n), due to the for loop which goes through all numbers from 1 to n.

The Java code for the above logic is as follows:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int largestDivisor(int n) {
        for (int i = n-1; i > 0; i--) {
            if (n % i == 0) {
                return i;
            }
        }
        return -1; // should never reach here
    }
}
```

In the main method, you can call this function with a number like this:

```java
public static void main (String[] args) {
    Solution solution = new Solution();
    int largestDivisor = solution.largestDivisor(15);
    System.out.println(largestDivisor);  // output: 5
}
```

This will print 5, which is the largest number that divides 15 evenly.
*/

class Main {
  public static void main(String[] args) {
    Solution solution = new Solution();
    int largestDivisor = solution.largestDivisor(15);
    System.out.println(largestDivisor);  // output: 5
  }
}

// The output should be 5 as the largest divisor of 15 is 5.

// The time complexity of this solution is O(n), because we are iterating from n-1 down to 1.

// The space complexity is O(1), as we are not using any additional data structures that scale with the size of the input.

// The