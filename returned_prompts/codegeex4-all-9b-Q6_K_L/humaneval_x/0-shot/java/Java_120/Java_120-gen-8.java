```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> maximum(List<Integer> arr, int k) {
        if (k == 0) {
            return new ArrayList<>();
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int num : arr) {
            pq.add(num);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        List<Integer> result = new ArrayList<>();
        while (!pq.isEmpty()) {
            result.add(pq.poll());
        }
        Collections.sort(result);
        return result;
    }
}
```