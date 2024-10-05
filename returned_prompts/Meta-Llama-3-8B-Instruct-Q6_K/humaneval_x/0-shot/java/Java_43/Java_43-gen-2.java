Here is the solution for the problem:

```java
import java.util.*;

class Solution {
    public boolean pairsSumToZero(List<Integer> l) {
        Set<Integer> set = new HashSet<>(l);
        for (int num : set) {
            if (set.contains(-num) && num != 0) {
                return true;
            }
        }
        return false;
    }
}
```

Explanation:
This problem can be solved by using a HashSet to store the elements of the list. Then we iterate over the HashSet and for each element, we check if its negation exists in the HashSet. If it does, we return true because we have found two distinct elements that sum to zero. If we don't find such a pair after iterating over the entire HashSet, we return false.

The time complexity of this solution is O(n) where n is the number of elements in the list because we are making a single pass over the list. The space complexity is also O(n) because we are storing all the elements in the HashSet. 

The given test cases will return the correct results with this solution. For example, for the input `[2, 4, -5, 3, 5, 7]`, the function will return `true` because `-5` and `5` sum to zero, and for the input `[1]`, the function will return `false` because there is no pair of elements that sum to zero. 