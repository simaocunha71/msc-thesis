Here is a simple implementation of the function `f` in Java. It uses two helper functions, `factorial` and `sum` to calculate the factorial and the sum respectively. 

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> f(int n) {
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                list.add(factorial(i));
            } else {
                list.add(sum(i));
            }
        }
        return list;
    }

    private int factorial(int n) {
        int fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }

    private int sum(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}
```

This solution should work correctly for any input `n`. It calculates the factorial for even `i` and the sum for odd `i`.