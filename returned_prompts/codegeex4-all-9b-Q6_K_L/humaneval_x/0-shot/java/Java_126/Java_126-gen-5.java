Here is the Java code that solves the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isSorted(List<Integer> lst) {
        if (lst.size() < 2) {
            return true;
        }
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < lst.get(i - 1) || lst.get(i).equals(lst.get(i - 1))) {
                return false;
            }
        }
        return true;
    }
}
```

This code works by iterating through the list from the second element to the last one. If it finds an element that is less than the previous one, or equal to it, it returns false. If it finds all elements in ascending order, it returns true.