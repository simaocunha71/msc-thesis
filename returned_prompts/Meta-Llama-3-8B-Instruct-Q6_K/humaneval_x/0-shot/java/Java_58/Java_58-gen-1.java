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

The problem can be solved by converting the lists to sets, retaining common elements in one set, and then converting back to a list. Here is the Java solution:

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

This solution works as follows:

1. Convert the input lists `l1` and `l2` to sets `set1` and `set2` using `HashSet` constructor.
2. Use the `retainAll` method to keep only the elements that are common to both sets.
3. Convert the resulting set back to a list using `ArrayList` constructor.

The time complexity of this solution is O(n + m), where n and m are the sizes of the input lists, because set operations have a linear time complexity. The space complexity is also O(n + m) due to the creation of the sets. 

The output of the solution for the given test cases is:

```
[1, 5, 653]
[2, 3]
``` 