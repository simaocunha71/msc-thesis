Here is a possible solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortEven(List<Integer> l) {
        List<Integer> evenIndexes = new ArrayList<>();
        List<Integer> oddIndexes = new ArrayList<>();

        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                evenIndexes.add(l.get(i));
            } else {
                oddIndexes.add(l.get(i));
            }
        }

        Collections.sort(evenIndexes);

        List<Integer> result = new ArrayList<>();
        int evenIndex = 0, oddIndex = 0;

        for (int i = 0; i < l.size(); i++) {
            if (i % 2 == 0) {
                result.add(evenIndexes.get(evenIndex));
                evenIndex++;
            } else {
                result.add(oddIndexes.get(oddIndex));
                oddIndex++;
            }
        }

        return result;
    }
}
```

This solution works by first separating the even and odd indexed elements of the input list into two separate lists. It then sorts the even indexed list and creates a new list with the same structure as the input list, but with the even indexed elements sorted. Finally, it returns this new list.