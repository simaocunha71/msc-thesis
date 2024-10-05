Here is the solution to the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> sumProduct(List<Integer> numbers) {
        int sum = 0;
        int product = 1;
        
        for (int number : numbers) {
            sum += number;
            product *= number;
        }
        
        List<Integer> result = new ArrayList<>();
        result.add(sum);
        result.add(product);
        
        return result;
    }
}
```

In this solution, we initialize two variables `sum` and `product` to 0 and 1 respectively. Then we iterate over the list of numbers and add each number to `sum` and multiply each number with `product`. Finally, we create a list `result` and add `sum` and `product` to it, then return the `result` list. If the input list is empty, `sum` will remain 0 and `product` will remain 1, as required.