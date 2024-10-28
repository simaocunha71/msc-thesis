Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<Integer> rollingMax(List<Integer> numbers) {
        List<Integer> result = new ArrayList<>();
        int maxSoFar = Integer.MIN_VALUE;
        for (int num : numbers) {
            result.add(Math.max(num, maxSoFar));
            maxSoFar = Math.max(maxSoFar, num);
        }
        return result;
    }
}
```

Explanation:
We use a simple iterative approach to solve this problem. We iterate over the input list and for each number, we calculate the maximum between the current number and the maximum found so far. We update the maximum found so far with the current number. The result is a list where each element is the maximum number found until that moment in the sequence. 

For example, given the list [1, 2, 3, 2, 3, 4, 2], the rolling maximums are [1, 2, 3, 3, 3, 4, 4]. 

Time complexity: O(n), where n is the size of the input list. 
Space complexity: O(n), as we need to store the result in a list of the same size as the input list. 

This solution is efficient and easy to understand. It's a good example of how to solve a problem by iterating over the input data and keeping track of the maximum value seen so far. 