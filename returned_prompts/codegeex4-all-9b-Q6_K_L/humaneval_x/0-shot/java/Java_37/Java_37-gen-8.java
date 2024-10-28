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
        int j = 0;
        for (int i = 0; i < l.size(); i += 2) {
            l.set(i, evenIndicies.get(j++));
        }
        return l;
    }
}
```