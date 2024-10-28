The task is to filter a given list of values and return a new list containing only the integers from the original list.

Here's the solution in Java:
```java
import java.util.*;

class Solution {
    public List<Integer> filterIntegers(List<Object> values) {
        List<Integer> result = new ArrayList<>();
        for (Object value : values) {
            if (value instanceof Integer) {
                result.add((Integer) value);
            }
        }
        return result;
    }
}
```
This solution uses an enhanced for loop to iterate over the input list. For each element, it checks if the element is an instance of `Integer` using the `instanceof` keyword. If it is, it adds the element to the result list. Finally, it returns the result list.

You can test this solution with the given examples:
```java
public static void main(String[] args) {
    Solution solution = new Solution();
    List<Object> values1 = Arrays.asList('a', 3.14, 5);
    List<Integer> result