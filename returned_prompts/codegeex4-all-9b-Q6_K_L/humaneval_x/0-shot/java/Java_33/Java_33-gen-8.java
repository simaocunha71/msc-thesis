```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortThird(List<Integer> l) {
        List<Integer> result = new ArrayList<>(l);
        List<Integer> multiplesOfThree = new ArrayList<>();

        for (int i = 0; i < result.size(); i++) {
            if (i % 3 == 0) {
                multiplesOfThree.add(result.get(i));
            }
        }

        Collections.sort(multiplesOfThree);

        for (int i = 0, j = 0; i < result.size(); i++) {
            if (i % 3 == 0) {
                result.set(i, multiplesOfThree.get(j));
                j++;
            }
        }

        return result;
    }
}
```