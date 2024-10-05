Here is the Java implementation for the function `f`:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> f(int n) {
        List<Integer> result = new ArrayList<>(n);
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(factorial(i));
            } else {
                result.add(sumOfNumbers(i));
            }
        }
        return result;
    }

    private int factorial(int num) {
        int result = 1;
        for (int i = 1; i <= num; i++) {
            result *= i;
        }
        return result;
    }

    private int sumOfNumbers(int num) {
        int result = 0;
        for (int i = 1; i <= num; i++) {
            result += i;
        }
        return result;
    }
}
```

In this implementation, we first initialize an empty list of size `n`. Then, we iterate through the numbers from 1 to `n`. For each number, we check if it's even or odd. If it's even, we calculate its factorial and add it to the list. If it's odd, we calculate the sum of numbers from 1 to `i` and add it to the list. Finally, we return the list.