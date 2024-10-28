        Map<Integer, Long> counts = numbers.stream()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        return numbers.stream()
                .filter(n -> counts.get(n) == 1)
                .collect(Collectors.toList());
    }
}

This code uses the Java Stream API to count the occurrences of each number and then filters out the ones that occur more than once.
The counts are stored in a Map, with the numbers as keys and the counts as values. The filter operation then uses these counts to keep only the numbers that occur exactly once.

The time complexity of this solution is O(N), where N is the number of elements in the list. This is because we perform two passes over the list: the first pass counts the occurrences and the second pass filters the elements. The space complexity is also O(N) because we store the counts of each number.

This solution assumes that the input list does not contain null elements. If the list can contain null, you would need to modify the code to handle that case.

If you want to maintain the order of elements, you can use a LinkedHashMap instead of a regular HashMap. This will keep the order of elements as they are encountered. But this solution will have a higher space complexity because it needs to store the order of elements.

And if you want to remove the duplicates in-place, i.e., modify the original list, you can use a two-pointer approach. The first pointer iterates over the list, and the second pointer marks the position of the next non-duplicate element. The time complexity of this solution is O(N), and the space complexity is O(1), but it modifies the original list.

You can choose the solution that best suits your needs.


A: You can use a HashMap to count occurrences of numbers and then iterate through the list again to remove numbers that occurred more than once.

Here's a possible solution:

```java
import java.util.*;

public class Solution {

    public List<Integer> removeDuplicates(List<Integer> numbers) {
        Map<Integer, Integer> counts = new HashMap<>();

        // Count occurrences
        for (int num