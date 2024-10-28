```java
import java.util.*;

class Solution {
    public List<Integer> maximum(List<Integer> arr, int k) {
        // Create a priority queue to store the k maximum numbers
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);

        // Add all elements from the array to the max heap
        for (int num : arr) {
            maxHeap.offer(num);
            // If the size of the max heap is greater than k, remove the smallest element
            if (maxHeap.size() > k) {
                maxHeap.poll();
            }
        }

        // Convert the max heap to a sorted list
        List<Integer> result = new ArrayList<>();
        while (!maxHeap.isEmpty()) {
            result.add(maxHeap.poll());
        }

        // Reverse the list because we added elements in ascending order
        Collections.reverse(result);

        return result;
    }
}
```


Explanation:
The problem can be solved by using a priority queue (max heap) to store the k maximum numbers. 

1.  We create a priority queue `maxHeap` with a comparator that compares elements in descending order.
2.  We iterate through the input array and add each element to the max heap.
3.  If the size of the max heap exceeds k, we remove the smallest element (which is the k-th largest element) to maintain the size of k.
4.  After adding all elements from the array, we convert the max heap to a sorted list by repeatedly removing and adding elements to the list.
5.  Finally, we reverse the list to get the k maximum numbers in ascending order.

The time complexity of this solution is O(n log k), where n is the size of the input array. This is because we add each element to the max heap in O(log k) time and we do this n times. The space complexity is O(k), as we store the k maximum numbers in the max heap. 