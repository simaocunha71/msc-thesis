```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<List<Integer>> getRow(List<List<Integer>> lst, int x) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    List<Integer> coords = new ArrayList<Integer>();
                    coords.add(i);
                    coords.add(j);
                    result.add(coords);
                }
            }
        }
        Collections.sort(result, new Comparator<List<Integer>>() {
            public int compare(List<Integer> a, List<Integer> b) {
                if (a.get(0) != b.get(0)) {
                    return a.get(0) - b.get(0);
                } else {
                    return b.get(1) - a.get(1);
                }
            }
        });
        return result;
    }
}
```
