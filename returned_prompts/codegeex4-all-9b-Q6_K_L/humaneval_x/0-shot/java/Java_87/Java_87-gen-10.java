```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<List<Integer>> getRow(List<List<Integer>> lst, int x) {
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < lst.size(); i++) {
            List<Integer> row = lst.get(i);
            for (int j = 0; j < row.size(); j++) {
                if (row.get(j) == x) {
                    List<Integer> coord = new ArrayList<>();
                    coord.add(i);
                    coord.add(j);
                    result.add(coord);
                }
            }
        }

        Collections.sort(result, new Comparator<List<Integer>>() {
            @Override
            public int compare(List<Integer> o1, List<Integer> o2) {
                if (o1.get(0) != o2.get(0)) {
                    return o1.get(0) - o2.get(0);
                } else {
                    return o2.get(1) - o1.get(1);
                }
            }
        });

        return result;
    }
}
```