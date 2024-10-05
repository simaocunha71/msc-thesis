```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortThird(List<Integer> l) {
        List<Integer> result = new ArrayList<>(l);
        List<Integer> indices = new ArrayList<>();

        for (int i = 2; i < result.size(); i += 3) {
            indices.add(result.get(i));
        }

        Collections.sort(indices);

        for (int i = 2; i < result.size(); i += 3) {
            result.set(i, indices.remove(0));
        }

        return result;
    }
}
```