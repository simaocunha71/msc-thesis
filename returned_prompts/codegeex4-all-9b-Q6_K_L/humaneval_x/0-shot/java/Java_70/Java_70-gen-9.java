```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        List<Integer> sortedList = new ArrayList<>(lst);
        Collections.sort(sortedList);
        List<Integer> result = new ArrayList<>();
        int i = 0;
        while (!sortedList.isEmpty()) {
            if (i % 2 == 0) {
                result.add(sortedList.remove(0));
            } else {
                result.add(sortedList.remove(sortedList.size() - 1));
            }
            i++;
        }
        return result;
    }
}
```