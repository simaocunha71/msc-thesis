        List<Integer> result = new ArrayList<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        maxHeap.addAll(arr);

        for (int i = 0; i < k; i++) {
            result.add(maxHeap.poll());
        }

        Collections.sort(result);
        return result;
    }
}

This solution creates a max heap from the input list and polls the max element from the heap k times. The result is a list of the k largest elements in the input list. The final step is to sort the list.

Time Complexity: O(n log n)
Space Complexity: O(n)
*/

//src/main/java/com/company/task14/Task14.java
package com.company.task14;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

public class Task14 {

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1
        List<Integer> arr1 = Arrays.asList(-3, -4, 5);
        int k1 = 3;
        System.out.println("Expected: [-4, -3, 5]");
        System.out.println("Actual: " + solution.maximum(arr1, k1));

        // Test case 2
        List<Integer> arr2 = Arrays.asList(4, -4, 4);
        int k2 = 2;
        System.out.println("Expected: [4, 4]");
        System.out.println("Actual: " + solution.maximum(arr2, k2));

        // Test case 3
        List<Integer> arr3 = Arrays.asList(-3, 2, 1, 2, -1, -2, 1);
        int k3 = 1;
        System.out.println("Expected: [2]");
        System.