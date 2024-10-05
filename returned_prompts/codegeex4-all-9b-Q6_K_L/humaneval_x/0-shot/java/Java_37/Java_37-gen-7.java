```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortEven(List<Integer> l) {
        if (l.size() < 2) {
            return l;
        }

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
The solution works by first extracting the even indexed elements of the input list into a separate list and sorting it. Then, it replaces the even indexed elements of the input list with the sorted even indexed elements.