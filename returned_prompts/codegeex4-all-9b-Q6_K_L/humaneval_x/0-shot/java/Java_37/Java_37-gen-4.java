```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sortEven(Arrays.asList(1, 2, 3))
    [1, 2, 3]
    >>> sortEven(Arrays.asList(5, 6, 3, 4))
    [3, 6, 5, 4]
     */
    public List<Integer> sortEven(List<Integer> l) {
        List<Integer> evenIndices = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            evenIndices.add(l.get(i));
        }
        Collections.sort(evenIndices);

        List<Integer> result = new ArrayList<>(l);
        for (int i = 0; i < evenIndices.size(); i++) {
            result.set(i * 2, evenIndices.get(i));
        }
        return result;
    }
}
```