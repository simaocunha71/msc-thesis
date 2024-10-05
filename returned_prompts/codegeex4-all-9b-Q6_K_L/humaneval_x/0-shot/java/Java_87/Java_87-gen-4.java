```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<List<Integer>> getRow(List<List<Integer>> lst, int x) {
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            List<Integer> row = lst.get(i);
            for (int j = row.size() - 1; j >= 0; j--) {
                if (row.get(j) == x) {
                    ans.add(Arrays.asList(i, j));
                }
            }
        }
        return ans;
    }
}
```