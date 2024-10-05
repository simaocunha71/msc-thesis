The task is to create a function named nextSmallest() that takes a list of integers as input and returns the 2nd smallest element of the list. If the list is empty or has only one element, the function should return an empty optional.

Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst.size() < 2) {
            return Optional.empty();
        }
        lst.sort(Comparator.naturalOrder());
        Optional<Integer> smallest = Optional.of(lst.get(0));
        Optional<Integer> nextSmallest = Optional.empty();
        for (int i = 1; i < lst.size(); i++) {
            if (!smallest.isPresent() || lst.get(i) != smallest.get()) {
                nextSmallest = Optional.of(lst.get(i));
                break;
            }
        }
        return nextSmallest;
    }
}
```
Explanation:

*   We first check if the list has less than 2 elements. If it does, we return an empty optional because there is no 2nd smallest element.
*   We sort the list in ascending order.
*   We initialize the smallest and nextSmallest options to empty. We then iterate over the list starting from the second element (index 1).
*   If the current element is not equal to the smallest element, we update the nextSmallest option with the current element. We break the loop because we have found the 2nd smallest element.
*   Finally, we return the nextSmallest option. If the list was empty or had only one element, the function returns an empty optional. Otherwise, it returns the 2nd smallest element wrapped in an optional.