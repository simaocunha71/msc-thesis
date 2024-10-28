Here is the solution using Java:

```java
import java.util.*;

class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        Set<Integer> set1 = new HashSet<>(l1);
        Set<Integer> set2 = new HashSet<>(l2);
        set1.retainAll(set2);
        return new ArrayList<>(set1);
    }
}
```

This solution first converts the lists to sets. Then, it uses the retainAll method to keep only the elements that are common to both sets. Finally, it converts the set back to a list and returns it.

You can test this method using the following code:

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

This code will print:

```
[1, 5, 653]
[2, 3]
```

Which are the common elements in the two lists.