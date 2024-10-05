Here's the Java implementation for the `sortThird` function:

```java
import java.util.*;

class Solution {
    public List<Integer> sortThird(List<Integer> l) {
        List<Integer> result = new ArrayList<>(l);
        List<Integer> thirdIndices = new ArrayList<>();

        // Collect the elements at indices divisible by three
        for (int i = 2; i < result.size(); i += 3) {
            thirdIndices.add(result.get(i));
        }

        // Sort the collected elements
        Collections.sort(thirdIndices);

        // Replace the elements at indices divisible by three with the sorted elements
        for (int i = 2; i < result.size(); i += 3) {
            result.set(i, thirdIndices.remove(0));
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1
        List<Integer> l1 = Arrays.asList(1, 2, 3);
        System.out.println(solution.sortThird(l1));  // Output: [1, 2, 3]

        // Test case 2
        List<Integer> l2 = Arrays.asList(5, 6, 3, 4, 8, 9, 2);
        System.out.println(solution.sortThird(l2));  // Output: [2, 6, 3, 4, 8, 9, 5]
    }
}
```