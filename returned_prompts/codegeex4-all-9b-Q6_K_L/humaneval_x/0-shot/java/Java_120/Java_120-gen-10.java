```java
import java.util.*;

class Solution {
    public List<Integer> maximum(List<Integer> arr, int k) {
        if (arr == null || arr.size() == 0 || k <= 0) {
            return new ArrayList<>();
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int num : arr) {
            pq.offer(num);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        List<Integer> result = new ArrayList<>();
        while (!pq.isEmpty()) {
            result.add(pq.poll());
        }
        Collections.sort(result, Collections.reverseOrder());
        return result;
    }
}
```