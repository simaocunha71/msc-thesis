```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        if (lst.size() == 0) {
            return lst;
        }

        List<Integer> res = new ArrayList<>();
        int min = Collections.min(lst);
        int max = Collections.max(lst);

        while (lst.size() > 1) {
            if (lst.contains(min)) {
                lst.remove(Integer.valueOf(min));
                res.add(min);
            }
            if (lst.contains(max)) {
                lst.remove(Integer.valueOf(max));
                res.add(max);
            }
        }
        if (lst.size() == 1) {
            res.add(lst.get(0));
        }
        return res;
    }
}
```