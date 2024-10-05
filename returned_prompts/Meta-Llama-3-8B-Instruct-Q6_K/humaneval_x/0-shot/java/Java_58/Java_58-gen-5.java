Here is a Java solution:

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

The solution uses two sets to store the elements from the two lists. The `retainAll` method is used to keep only the elements that are common to both sets. The result is then converted to a list and sorted. This solution has a time complexity of O(n log n) due to the sorting, where n is the total number of elements in the two lists. The space complexity is O(n) due to the use of two sets and a list. 

The unit test case is also provided:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    List<Integer> l1 = Arrays.asList(1, 4, 3, 34, 653, 2, 5);
    List<Integer> l2 = Arrays.asList(5, 7, 1, 5, 9, 653, 121);
    List<Integer> result = solution.common(l1, l2);
    System.out.println(result);

    l1 = Arrays.asList(5, 3, 2, 8);
    l2 = Arrays.asList(3, 2);
    result = solution.common(l1, l2);
    System.out.println(result);
}
```

The output will be:

```
[1, 5, 653]
[2, 3]
``` 