Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<List<Integer>> getRow(List<List<Integer>> lst, int x) {
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = lst.get(i).size() - 1; j >= 0; j--) {
                if (lst.get(i).get(j) == x) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }
        Collections.sort(result, (a, b) -> Integer.compare(a.get(0), b.get(0)));
        return result;
    }
}
```

This solution iterates over the input list and its sublists to find the coordinates of the number x. It uses a list of lists to store these coordinates. The coordinates are added to the result list in the order they are found. After all coordinates are found, the list is sorted by the row number in ascending order.

The time complexity of this solution is O(n*m), where n is the number of rows and m is the maximum number of columns in the input list. The space complexity is O(n*m) as well, for storing the result. 