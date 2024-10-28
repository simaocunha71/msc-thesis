```java
import java.util.*;

class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        if (lst.isEmpty()) {
            return lst;
        }

        List<Integer> result = new ArrayList<>();
        List<Integer> temp = new ArrayList<>(lst);

        while (!temp.isEmpty()) {
            int min = Collections.min(temp);
            result.add(min);
            temp.remove((Integer) min);

            if (!temp.isEmpty()) {
                int max = Collections.max(temp);
                result.add(max);
                temp.remove((Integer) max);
            }
        }

        return result;
    }
}
```
Explanation:
The problem is asking to sort a list of integers in a "strange" order. The order is defined as follows: start with the minimum value, then take the maximum of the remaining integers, then the minimum again, and so on.

Here is a Java solution for this problem:

First, we check if the input list is empty. If it is, we simply return the empty list.

Then, we create a copy of the input list and an empty list to store the result. We iterate over the copied list until it is empty.

In each iteration, we find the minimum value in the copied list and add it to the result list. We then remove this value from the copied list.

If the copied list is not empty after removing the minimum value, we find the maximum value in the copied list and add it to the result list. We then remove this value from the copied list.

Finally, we return the result list.

This solution works by iterating over the input list in a specific order, which is defined by the problem. It uses the `Collections.min` and `Collections.max` methods to find the minimum and maximum values in the list, and the `remove` method to remove these values from the list. It also uses an empty list to store the result, which is returned at the end of the method.