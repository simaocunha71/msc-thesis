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
This solution iterates through the list of lists, and for each row, it iterates through the columns from right to left. If it finds an element equal to `x`, it adds the coordinates to the result list. After that, it sorts the result list based on the row index in ascending order. The sorting is done using the `Collections.sort` method with a custom comparator that compares the row indices. The `get` method is used to get the elements of the lists. The `Arrays.asList` method is used to convert the coordinates to a list. The `Integer.compare` method is used to compare the row indices. The `return` statement returns the result list.