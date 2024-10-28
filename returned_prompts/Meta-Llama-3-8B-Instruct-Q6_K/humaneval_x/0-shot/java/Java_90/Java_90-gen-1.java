The problem asks you to write a function that returns the 2nd smallest element in a list of integers. If the list contains less than 2 unique elements, it should return an empty optional.

Here is the solution:
```java
import java.util.*;
import java.util.Optional;

public class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        List<Integer> uniqueList = new ArrayList<>();
        for (int num : lst) {
            if (!uniqueList.contains(num)) {
                uniqueList.add(num);
            }
        }
        if (uniqueList.size() < 2) {
            return Optional.empty();
        }
        Collections.sort(uniqueList);
        return Optional.of(uniqueList.get(1));
    }
}
```
This solution first creates a new list that contains only unique elements from the input list. Then it checks if the new list contains at least 2 elements. If not, it returns an empty optional. If the list contains at least 2 elements, it sorts the list and returns the 2nd element as an optional. 

The time complexity of this solution is O(n log n) due to the sorting operation, where n is the number of unique elements in the list. The space complexity is O(n) for storing the unique elements in a new list. 