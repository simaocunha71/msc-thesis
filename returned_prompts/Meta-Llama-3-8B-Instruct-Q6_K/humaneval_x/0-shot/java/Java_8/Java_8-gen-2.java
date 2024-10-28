Here is the solution:
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
Explanation:

*   We iterate over the list of integers using a for-each loop.
*   We initialize two variables, `sum` and `product`, to 0 and 1 respectively.
*   In each iteration, we add the current number to the `sum` and multiply the current number with the `product`.
*   After the loop, we create a new list `result` and add the calculated `sum` and `product` to it.
*   Finally, we return the `result` list.

This solution correctly handles the edge case where the input list is empty, as it initializes the `sum` to 0 and `product` to 1, according to the problem statement. The resulting list will have the correct sum and product for the input list.