Here is a Java solution that uses a HashSet to remove duplicates and a List to store the common elements.

```java
import java.util.*;

class Solution {
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
This solution has a time complexity of O(n) where n is the total number of elements in the two lists. The space complexity is O(n) as well, where n is the number of unique elements in the two lists.

The `retainAll` method is used to keep only the elements that are present in both sets. The `ArrayList` is used to store the result, and the `Collections.sort` method is used to sort the result in ascending order.

You can test this solution using the following code:

```java
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> l1 = Arrays.asList(1, 4, 3, 34, 653, 2, 5);
        List<Integer> l2 = Arrays.asList(5, 7, 1, 5, 9, 653, 121);
        List<Integer> result = solution.common(l1, l2);
        System.out.println(result);
    }
}
```
This will output: `[1, 5, 653]`

You can also test it with other examples, such as:

```java
List<Integer> l1 = Arrays.asList(5, 3, 2, 8);
List<Integer> l2 = Arrays.asList(3, 2);
List<Integer> result = solution.common(l1, l2);
System.out.println(result);
```
This will output: `[2, 3]`  ######



Explanation:

*   We create two sets, `set1` and `set2`, from the input lists `l1` and `l2` respectively.
*   We use the `retainAll` method to keep only the elements that are present in both sets.
*   We create a new `ArrayList` called `result` and add all the elements from `set1` to it.
*   We sort the `result` list