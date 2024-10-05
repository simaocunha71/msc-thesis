```java
import java.util.*;
import java.util.stream.*;

class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst.size() < 2) {
            return Optional.empty();
        }
        lst.sort(Comparator.naturalOrder());
        int secondSmallest = lst.get(1);
        for (int i = 2; i < lst.size(); i++) {
            if (lst.get(i) < secondSmallest) {
                return Optional.of(lst.get(i));
            }
        }
        return Optional.of(secondSmallest);
    }
}
```

Explanation:
The problem requires you to find the 2nd smallest element in a list of integers. If there is no such element (i.e., all elements are the same), return an empty Optional.

Here's the solution:

1. First, we check if the list has less than 2 elements. If it does, we return an empty Optional, as there is no 2nd smallest element.

2. Next, we sort the list in ascending order.

3. We then find the 2nd smallest element by comparing each element starting from the 2nd element. If we find an element that is smaller than the current 2nd smallest element, we return that element.

4. If we reach the end of the list without finding a smaller element, it means the 2nd smallest element is the last element we checked, so we return that element.

Note that we use Optional to return the result, which allows us to return null if there is no 2nd smallest element. The Optional class is part of the Java Stream API. We use its of() method to create an Optional instance from a value, and its empty() method to create an empty Optional instance.