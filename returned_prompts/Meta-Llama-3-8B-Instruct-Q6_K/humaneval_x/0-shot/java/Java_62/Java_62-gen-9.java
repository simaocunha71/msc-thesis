Here is the solution in Java. It calculates the derivative of a polynomial represented as a list of coefficients.

```java
import java.util.*;

class Solution {
    public List<Integer> derivative(List<Integer> xs) {
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i < xs.size(); i++) {
            result.add(xs.get(i) * i);
        }
        return result;
    }
}
```

This solution iterates over the list of coefficients starting from the second element (index 1) and calculates the derivative by multiplying each coefficient with its index. The result is a new list of coefficients representing the derivative of the polynomial.

For example, if the input list is `[3, 1, 2, 4, 5]`, the output will be `[1, 4, 12, 20]`. If the input list is `[1, 2, 3]`, the output will be `[2, 6]`. The time complexity is O(n), where n is the size of the input list, and the space complexity is also O(n) for the result list.