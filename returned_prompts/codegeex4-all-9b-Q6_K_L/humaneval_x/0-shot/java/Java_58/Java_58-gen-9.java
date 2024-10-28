```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        Set<Integer> s1 = new HashSet<>(l1);
        Set<Integer> s2 = new HashSet<>(l2);
        s1.retainAll(s2);
        List<Integer> result = new ArrayList<>(s1);
        Collections.sort(result);
        return result;
    }
}
```