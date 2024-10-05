```java
import java.util.*;

class Solution {
    public List<Integer> maximum(List<Integer> arr, int k) {
        // Use a priority queue to store the k largest elements
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);

        for (int num : arr) {
            // Add the number to the priority queue
            pq.offer(num);

            // If the priority queue has more than k elements, remove the smallest one
            if (pq.size() > k) {
                pq.poll();
            }
        }

        // Create a list to store the k largest elements
        List<Integer> result = new ArrayList<>();

        // Add the k largest elements to the list
        for (int i = 0; i < k; i++) {
            result.add(pq.poll());
        }

        // Sort the list in ascending order
        Collections.sort(result);

        return result;
    }
}
```


Explanation:

1. We use a priority queue to store the k largest elements. The priority queue is ordered in descending order, so the largest element is always at the top.
2. We iterate through the array and add each element to the priority queue.
3. If the priority queue has more than k elements, we remove the smallest one to keep the size of the queue at k.
4. We create a list to store the k largest elements and add the elements from the priority queue to the list.
5. We sort the list in ascending order and return it.

The time complexity of this solution is O(n log k), where n is the length of the array. This is because we iterate through the array once and use a priority queue with a size of k. The space complexity is O(k), as we store the k largest elements in the priority queue and the result list.