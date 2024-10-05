```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortThird(List<Integer> l) {
        List<Integer> result = new ArrayList<>();
        List<Integer> divisibleByThree = new ArrayList<>();
        
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                divisibleByThree.add(l.get(i));
            }
        }
        
        Collections.sort(divisibleByThree);
        
        int j = 0;
        for (int i = 0; i < l.size(); i++) {
            if (i % 3 == 0) {
                result.add(divisibleByThree.get(j));
                j++;
            } else {
                result.add(l.get(i));
            }
        }
        
        return result;
    }
}
```