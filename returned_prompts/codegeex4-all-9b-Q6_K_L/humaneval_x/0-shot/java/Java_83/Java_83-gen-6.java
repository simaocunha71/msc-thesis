To solve this problem, we need to understand the pattern of numbers that start or end with 1. For example, if n is 2, the numbers are 10, 11, 12, ..., 19, 101, 102, ..., 109, 111, ..., 199. Notice that the numbers that start with 1 are from 10 to 19 and from 100 to 109. The numbers that end with 1 are from 11 to 19 and from 101 to 199.

For a given n, the count of numbers that start with 1 is 9 * 10^(n-2) because the first digit is fixed as 1 and the remaining n-1 digits can be any digit from 0 to 9. Similarly, the count of numbers that end with 1 is also 9 * 10^(n-2).

Therefore, the total count of numbers that start or end with 1 is 9 * 10^(n-2) + 9 * 10^(n-2) = 18 * 10^(n-2).

Here is the updated solution:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int startsOneEnds(int n) {
        return 18 * Math.pow(10, n-2);
    }
}
```

This solution uses the Math.pow() function to calculate 10^(n-2) and then multiplies it by 18 to get the total count.