Here is a simple and efficient solution in Java. This solution first converts the lists to sets, then finds the intersection of the two sets, and finally converts the intersection back to a list.

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

This solution has a time complexity of O(n log n) due to the sorting at the end, where n is the size of the smaller list. The space complexity is O(n) for storing the result. 

If you don't need to sort the result, you can remove the sorting step and the time complexity will be reduced to O(n). 

You can test this solution with the following main method:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    List<Integer> l1 = Arrays.asList(1, 4, 3, 34, 653, 2, 5);
    List<Integer> l2 = Arrays.asList(5, 7, 1, 5, 9, 653, 121);
    List<Integer> result = solution.common(l1, l2);
    System.out.println(result);
}
```

This will output: `[1, 5, 653]` which is the sorted unique common elements for the two lists. 