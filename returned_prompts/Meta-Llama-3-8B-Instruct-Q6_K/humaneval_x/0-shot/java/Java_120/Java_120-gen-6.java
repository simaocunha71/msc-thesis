Here is a Java solution that uses a priority queue to solve the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> maximum(List<Integer> arr, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        List<Integer> result = new ArrayList<>();

        for (int num : arr) {
            pq.offer(num);
            if (pq.size() > k) {
                pq.poll();
            }
        }

        while (!pq.isEmpty()) {
            result.add(pq.poll());
        }

        Collections.reverse(result);
        return result;
    }
}
```

In this solution, we create a priority queue that always stores the maximum k numbers in descending order. We iterate through the input array and add each number to the priority queue. If the size of the priority queue exceeds k, we remove the smallest element (which is the k-th largest number) from the queue.

After processing all the numbers, we extract the k maximum numbers from the priority queue and store them in a list. We reverse the list to get the correct order (from largest to smallest) and return it.

The time complexity of this solution is O(n log k), where n is the length of the input array. The space complexity is O(k), as we need to store the k maximum numbers in the priority queue.