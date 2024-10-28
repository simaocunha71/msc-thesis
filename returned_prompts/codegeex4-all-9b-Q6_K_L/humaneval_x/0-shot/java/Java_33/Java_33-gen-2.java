```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortThird(List<Integer> l) {
        List<Integer> result = new ArrayList<>();
        List<Integer> indices = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                indices.add(l.get(i));
            }
        }
        Collections.sort(indices);
        int index = 0;
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                result.add(indices.get(index++));
            } else {
                result.add(l.get(i));
            }
        }
        return result;
    }
}
```