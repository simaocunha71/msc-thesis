```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortThird(List<Integer> l) {
        List<Integer> out = new ArrayList<>(l);
        List<Integer> toSort = new ArrayList<>();
        for (int i = 0; i < out.size(); i++) {
            if (i % 3 == 0) {
                toSort.add(out.get(i));
            }
        }
        Collections.sort(toSort);
        int j = 0;
        for (int i = 0; i < out.size(); i++) {
            if (i % 3 == 0) {
                out.set(i, toSort.get(j));
                j++;
            }
        }
        return out;
    }
}
```