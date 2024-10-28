```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortEven(List<Integer> l) {
        List<Integer> even = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            even.add(l.get(i));
        }
        Collections.sort(even);
        for (int i = 0, j = 0; i < l.size(); i += 2) {
            l.set(i, even.get(j++));
        }
        return l;
    }
}
```