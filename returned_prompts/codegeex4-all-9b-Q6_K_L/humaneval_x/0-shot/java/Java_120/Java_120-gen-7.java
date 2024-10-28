```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> maximum(List<Integer> arr, int k) {
        List<Integer> result = new ArrayList<>();
        if (k == 0) {
            return result;
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int num : arr) {
            pq.offer(num);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        while (!pq.isEmpty()) {
            result.add(pq.poll());
        }
        Collections.sort(result);
        return result;
    }
}
```
This solution uses a priority queue to keep track of the maximum k numbers in the array. It first adds all the numbers in the array to the priority queue. If the size of the priority queue exceeds k, it removes the smallest number. Finally, it sorts the result and returns it.