```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> unique(List<Integer> l) {
        Set<Integer> set = new HashSet<>(l);
        List<Integer> result = new ArrayList<>(set);
        Collections.sort(result);
        return result;
    }
}
```