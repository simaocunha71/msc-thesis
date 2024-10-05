Here is a Java solution to your problem:

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
        for (int i = 2; i <= n; i++) {
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

This solution first initializes an empty list. It then iterates through all integers from 1 to n. For each integer, it checks if it is even or odd. If the integer is even, it calculates and adds the factorial of the integer to the list. If the integer is odd, it calculates and adds the sum of all integers from 1 to the integer to the list. The `factorial` and `sum` methods are helper methods that calculate the factorial and sum of all integers from 1 to a given integer, respectively.