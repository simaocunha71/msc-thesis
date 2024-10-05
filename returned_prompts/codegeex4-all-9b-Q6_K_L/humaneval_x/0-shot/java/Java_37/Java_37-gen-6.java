Here's the Java implementation for the `sortEven` function:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortEven(List<Integer> l) {
        List<Integer> evenIndicies = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            evenIndicies.add(l.get(i));
        }
        Collections.sort(evenIndicies);
        for (int i = 0, j = 0; i < l.size(); i += 2) {
            l.set(i, evenIndicies.get(j++));
        }
        return l;
    }
}
```

This function works by first creating a new list `evenIndicies` that contains the values at the even indices of the input list `l`. It then sorts this list in ascending order.

The function then iterates over the even indices of the input list `l` and replaces each value with the corresponding value from the sorted `evenIndicies` list.

Finally, the function returns the modified list `l`.