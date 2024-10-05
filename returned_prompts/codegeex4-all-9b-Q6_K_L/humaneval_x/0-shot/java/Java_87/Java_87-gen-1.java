Here is the solution:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<List<Integer>> getRow(List<List<Integer>> lst, int x) {
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }
        Collections.sort(result, new Comparator<List<Integer>>() {
            @Override
            public int compare(List<Integer> o1, List<Integer> o2) {
                if (o1.get(0) < o2.get(0)) {
                    return -1;
                } else if (o1.get(0) > o2.get(0)) {
                    return 1;
                } else {
                    if (o1.get(1) > o2.get(1)) {
                        return -1;
                    } else if (o1.get(1) < o2.get(1)) {
                        return 1;
                    } else {
                        return 0;
                    }
                }
            }
        });
        return result;
    }
}
```
This solution iterates over the nested list and checks if the element is equal to x. If it is, it adds the coordinates to the result list. After that, it sorts the result list based on the row and column numbers.