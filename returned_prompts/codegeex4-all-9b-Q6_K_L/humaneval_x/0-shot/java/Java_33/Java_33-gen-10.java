```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortThird(List<Integer> l) {
        List<Integer> result = new ArrayList<>(l);
        List<Integer> thirdIndices = new ArrayList<>();
        for (int i = 0; i < result.size(); i += 3) {
            thirdIndices.add(result.get(i));
        }
        Collections.sort(thirdIndices);
        for (int i = 0, j = 0; i < result.size(); i += 3) {
            result.set(i, thirdIndices.get(j++));
        }
        return result;
    }
}
```