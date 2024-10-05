Here is a Java solution using the `List` interface and `Collections` utility class:

```java
import java.util.*;

class Solution {
    public String exchange(List<Integer> lst1, List<Integer> lst2) {
        List<Integer> lst1Copy = new ArrayList<>(lst1);
        for (Integer num : lst1Copy) {
            if (num % 2 != 0) {
                int index = lst1Copy.indexOf(num);
                lst1Copy.set(index, lst2.remove(0));
            }
        }
        for (Integer num : lst1Copy) {
            if (num % 2 != 0) {
                return "NO";
            }
        }
        return "YES";
    }
}
```

In this solution, we first create a copy of `lst1` and then iterate over it. If we find an odd number, we remove the first element from `lst2` and replace the odd number in `lst1` with the removed element. We repeat this process until all elements in `lst1` are even. If after this process, we still find an odd number in `lst1`, we return "NO". Otherwise, we return "YES". This solution has a time complexity of O(n), where n is the size of `lst1` and `lst2`. It uses O(n) extra space to store the copy of `lst1`. 