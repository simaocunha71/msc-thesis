Here is the solution:
```java
import java.util.*;

class Solution {
    public List<Integer> intersperse(List<Integer> numbers, int delimiter) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < numbers.size(); i++) {
            result.add(numbers.get(i));
            if (i < numbers.size() - 1) {
                result.add(delimiter);
            }
        }
        return result;
    }
}
```
Here's an explanation of the solution:

The problem asks to insert a number 'delimeter' between every two consecutive elements of the input list `numbers`. We can achieve this by iterating over the list and adding each element to the result list, and then adding the delimiter if we're not at the last element of the list.

In the code above, we create a new list `result` to store the output. We then iterate over the input list `numbers` using a for loop. For each element, we add it to the `result` list. If we're not at the last element of the list, we add the delimiter to the `result` list.

Finally, we return the `result` list. The time complexity of this solution is O(n), where n is the size of the input list, since we iterate over the list once. The space complexity is also O(n), since we store the output in a new list.