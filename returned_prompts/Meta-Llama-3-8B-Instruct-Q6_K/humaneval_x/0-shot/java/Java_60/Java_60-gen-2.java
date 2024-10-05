        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}
S:
The solution code is given below:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int sumToN(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}
```

This code defines a class `Solution` with a method `sumToN` that takes an integer `n` as input and returns the sum of all numbers from 1 to `n`.

The method uses a for loop to iterate from 1 to `n`, adding each number to the `sum` variable. Finally, the method returns the `sum` value.

The provided unit tests demonstrate the correctness of the method, verifying that the sum of numbers from 1 to `n` is correctly calculated for various values of `n`.

Note: This solution uses the naive approach of summing numbers from 1 to `n` using a for loop. For large values of `n`, this approach may be inefficient. A more efficient solution could use the formula for the sum of an arithmetic series, which is `n * (n + 1) / 2`. However, for small to moderate values of `n`, the provided solution is sufficient.