Here is the Java implementation of the function `f`:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> f(int n) {
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(factorial(i));
            } else {
                result.add(sum(i));
            }
        }
        return result;
    }

    private int factorial(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    private int sum(int n) {
        int result = 0;
        for (int i = 1; i <= n; i++) {
            result += i;
        }
        return result;
    }
}
```

This implementation first creates an empty list called `result`. It then iterates through the numbers from 1 to `n`. If the current number is even, it calculates the factorial of the number using the `factorial` method and adds the result to the list. If the current number is odd, it calculates the sum of the numbers from 1 to the current number using the `sum` method and adds the result to the list.

The `factorial` method calculates the factorial of a number by multiplying all the numbers from 1 to the number. The `sum` method calculates the sum of the numbers from 1 to a number by adding all the numbers from 1 to the number.

Finally, the function returns the list `result` which contains the results of the calculations.