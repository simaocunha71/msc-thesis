```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortEven(List<Integer> l) {
        List<Integer> result = new ArrayList<>(l);
        List<Integer> even = new ArrayList<>();
        for (int i = 0; i < result.size(); i += 2) {
            even.add(result.get(i));
        }
        Collections.sort(even);
        int j = 0;
        for (int i = 0; i < result.size(); i += 2) {
            result.set(i, even.get(j));
            j++;
        }
        return result;
    }
}
```