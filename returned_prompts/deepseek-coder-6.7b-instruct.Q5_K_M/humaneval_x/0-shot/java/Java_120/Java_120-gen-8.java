        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        maxHeap.addAll(arr);

        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < k; i++){
            result.add(maxHeap.poll());
        }

        Collections.sort(result);
        return result;
    }
}

Explanation:
Here we are using a priority queue with a Collections.reverseOrder comparator, which will give us a max heap. We add all the elements in the array to the heap and then poll the top k elements from the heap. These will be the k maximum elements in the array. We then sort the result and return it.

This solution has a time complexity of O(n log n) because of the sorting and the heap operations, where n is the size of the array. The space complexity is O(n) because of the space required for the heap.
*/

import java.util.*;

class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.maximum(Arrays.asList(-3, -4, 5), 3)); // [-4, -3, 5]
        System.out.println(s.maximum(Arrays.asList(4, -4, 4), 2)); // [4, 4]
        System.out.println(s.maximum(Arrays.asList(-3, 2, 1, 2, -1, -2, 1), 1)); // [2]
    }
}
```

## Conclusion
In this challenge, you learned how to use the PriorityQueue in Java to solve the problem. PriorityQueue is a class in Java that implements the Queue interface and provides an efficient way to maintain a collection of elements in sorted order.

You also learned about the Collections.reverseOrder() function which is used to reverse the natural ordering of the elements in the PriorityQueue.

This challenge helped you understand how to use PriorityQueue to find the k maximum elements in an array. It's a common problem in computer science and can