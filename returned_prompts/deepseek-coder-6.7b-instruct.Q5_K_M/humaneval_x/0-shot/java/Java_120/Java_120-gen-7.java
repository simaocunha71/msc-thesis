        List<Integer> result = new ArrayList<>();
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        queue.addAll(arr);
        for(int i = 0; i < k; i++){
            result.add(queue.poll());
        }
        Collections.sort(result);
        return result;
    }
}

Explanation:
This solution works by first adding all elements of the array to a priority queue, which will automatically sort the numbers in descending order. 

Then we poll the priority queue k times, which will remove the maximum element each time and add it to the result list. 

Finally, we sort the result list and return it. This solution has a time complexity of O(n log n) because of the sorting step, and a space complexity of O(n) for storing the priority queue.

The solution is correct because it returns a sorted list of the k maximum elements in the array, which is what the problem statement asks for.

It can be further optimized by using a min heap of size k and removing the minimum element from the heap whenever a new maximum element is found. This will have a time complexity of O(n log k) and a space complexity of O(k).

However, in this solution, we are assuming that the order of the elements in the array is not important, which is what the problem statement states.
 */

//C:
/*
public class Main {
    public static void main(String[] args) {
        List<Integer> arr = Arrays.asList(-3, -4, 5);
        int k = 3;
        Solution sol = new Solution();
        System.out.println(sol.maximum(arr, k));

        arr = Arrays.asList(4, -4, 4);
        k = 2;
        System.out.println(sol.maximum(arr, k));

        arr = Arrays.asList(-3, 2, 1, 2, -1, -2, 1);
        k = 1;
        System.out.println(sol.maximum(arr, k));
    }
}
*/
// This is a test class. It tests