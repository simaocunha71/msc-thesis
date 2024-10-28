Here is the Java code that returns the sorted unique common elements for two lists:
```java
import java.util.*;

public class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        Set<Integer> set1 = new HashSet<>(l1);
        Set<Integer> set2 = new HashSet<>(l2);
        set1.retainAll(set2);
        List<Integer> result = new ArrayList<>(set1);
        Collections.sort(result);
        return result;
    }
}
```
The `common` method takes two lists of integers as input and returns a sorted list of unique elements that are common to both lists. Here's a step-by-step breakdown of the implementation:

1. Create two `HashSet` objects `set1` and `set2` from the input lists `l1` and `l2`, respectively. This allows us to efficiently remove duplicates and perform set operations.
2. Use the `retainAll` method to retain only the elements that are common to both sets. This method modifies the original set by removing elements that are not present in the other set.
3. Create a new `ArrayList` object `result` from the modified set `set1`. This allows us to store the common elements in a list.
4. Sort the `result` list using the `Collections.sort` method.
5. Return the sorted `result` list.

You can test this method using the following code:
```java
public static void main(String[] args) {
    Solution solution = new Solution();
    List<Integer> l1 = Arrays.asList(1, 4, 3, 34, 653, 2, 5);
    List<Integer> l2 = Arrays.asList(5, 7, 1, 5, 9, 653, 121);
    List<Integer> result = solution.common(l1, l2);
    System.out.println(result); // [1, 5, 653]

    l1 = Arrays.asList(5, 3, 2, 8);
    l2 = Arrays.asList(3, 2);
    result = solution.common(l1, l2);
    System.out.println(result); // [2, 3]
}
```
This code creates two lists `l1` and `l2`, calls the `common` method to find the common elements, and prints the result. The output should match the expected results.