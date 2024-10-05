```java
import java.util.*;

class Solution {
    public List<Integer> sortEven(List<Integer> l) {
        List<Integer> evens = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            evens.add(l.get(i));
        }
        Collections.sort(evens);
        int j = 0;
        for (int i = 0; i < l.size(); i += 2) {
            l.set(i, evens.get(j++));
        }
        return l;
    }
}
```