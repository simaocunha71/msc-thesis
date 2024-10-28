Here is a Java solution that uses a priority queue to sort the list in the strange order:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        List<Integer> result = new ArrayList<>();

        for (int num : lst) {
            pq.offer(num);
        }

        boolean minFirst = true;
        while (!pq.isEmpty()) {
            if (minFirst) {
                result.add(pq.poll());
            } else {
                result.add(pq.poll());
            }
            minFirst = !minFirst;
        }

        return result;
    }
}
```
In this solution, we first add all the numbers in the list to a priority queue. Then we iterate through the priority queue, adding the smallest or largest number (depending on the value of `minFirst`) to the result list, and then flipping the value of `minFirst` to add the opposite number next. This results in a list that is sorted in the strange order.

The time complexity of this solution is O(n log n), where n is the number of elements in the input list, because we have to insert each element into the priority queue, which takes O(log n) time, and we do this for each element. The space complexity is O(n), because we have to store all the elements in the priority queue and the result list.