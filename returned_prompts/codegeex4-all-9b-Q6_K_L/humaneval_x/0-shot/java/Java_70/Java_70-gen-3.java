Here is a Java solution using a priority queue to get the minimum and maximum elements:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        if (lst == null || lst.isEmpty()) {
            return Collections.emptyList();
        }

        PriorityQueue<Integer> minQueue = new PriorityQueue<>(lst);
        PriorityQueue<Integer> maxQueue = new PriorityQueue<>(Collections.reverseOrder(lst));
        List<Integer> result = new ArrayList<>();

        while (!minQueue.isEmpty() && !maxQueue.isEmpty()) {
            result.add(minQueue.poll());
            result.add(maxQueue.poll());
        }

        while (!minQueue.isEmpty()) {
            result.add(minQueue.poll());
        }

        while (!maxQueue.isEmpty()) {
            result.add(maxQueue.poll());
        }

        return result;
    }
}
```

This solution works by creating two priority queues: one sorted in ascending order (minQueue) and one sorted in descending order (maxQueue). The main loop of the function then alternates between adding the smallest and largest remaining elements to the result list. If one of the queues becomes empty before the other, the remaining elements are added to the result list in order.