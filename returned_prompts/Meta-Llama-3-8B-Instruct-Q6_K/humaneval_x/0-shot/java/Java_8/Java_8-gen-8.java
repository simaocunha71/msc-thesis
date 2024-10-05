Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> sumProduct(List<Integer> numbers) {
        int sum = 0;
        int product = 1;
        for (int num : numbers) {
            sum += num;
            product *= num;
        }
        List<Integer> result = new ArrayList<>();
        result.add(sum);
        result.add(product);
        return result;
    }
}
```

This solution initializes two variables `sum` and `product` to 0 and 1 respectively. Then it iterates over the list of integers, adding each number to the `sum` and multiplying each number to the `product`. After that, it creates a new list `result` and adds the `sum` and `product` to it, and finally returns the `result`. If the input list is empty, the `sum` will be 0 and the `product` will be 1, as required.