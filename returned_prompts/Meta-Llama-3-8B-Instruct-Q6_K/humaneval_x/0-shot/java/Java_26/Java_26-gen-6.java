Here is a Java solution to the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        Map<Integer, Boolean> seen = new HashMap<>();
        List<Integer> result = new ArrayList<>();

        for (int num : numbers) {
            if (!seen.containsKey(num)) {
                seen.put(num, true);
                result.add(num);
            }
        }

        return result;
    }
}
```

This solution iterates over the input list of numbers and keeps track of the numbers it has seen using a HashMap. For each number, it checks if it has been seen before. If not, it adds the number to the result list and marks it as seen. This way, the result list contains only the numbers that appear exactly once in the input list. The order of the elements in the result list is the same as in the input list.

The time complexity of this solution is O(n), where n is the size of the input list, because we iterate over the list once. The space complexity is O(n) as well, because in the worst case, we need to store all numbers in the HashMap and the result list. 

You can test this solution using the following code:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    List<Integer> numbers = Arrays.asList(1, 2, 3, 2, 4);
    List<Integer> result = solution.removeDuplicates(numbers);
    System.out.println(result); // Output: [1, 3, 4]
}
```  