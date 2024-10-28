```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortEven(List<Integer> l) {
        ArrayList<Integer> evens = new ArrayList<>();
        for (int i = 0; i < l.size(); i += 2) {
            evens.add(l.get(i));
        }
        Collections.sort(evens);
        int index = 0;
        for (int i = 1; i < l.size(); i += 2) {
            l.set(i, evens.get(index++));
        }
        return l;
    }
}
```