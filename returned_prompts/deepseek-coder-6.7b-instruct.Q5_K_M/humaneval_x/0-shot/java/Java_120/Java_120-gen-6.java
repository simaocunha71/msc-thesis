        // Create a max heap for storing the k maximum numbers
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        maxHeap.addAll(arr);

        // Add the k maximum numbers to the result list
        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < k; i++) {
            result.add(maxHeap.poll());
        }

        // Sort the result list in ascending order
        Collections.sort(result);

        return result;
    }
}

This solution uses a max heap to store the k maximum numbers from the array. The time complexity of the solution is O(n log k), where n is the length of the array. The space complexity is O(k), since a max heap of size k is used.
*/

import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> maximum(List<Integer> arr, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        maxHeap.addAll(arr);

        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < k; i++) {
            result.add(maxHeap.poll());
        }

        Collections.sort(result);

        return result;
    }
}

/*
Test case 1:
Input: arr = [-3, -4, 5], k = 3
Output: [-4, -3, 5]

Test case 2:
Input: arr = [4, -4, 4], k = 2
Output: [4, 4]

Test case 3:
Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
Output: [2]
*/

/*
Test case 4:
Input: arr = [5, -5, -5, 3, 3, 3], k = 3
Output: [3, 3, 5]

Test case 5:
Input: arr = [