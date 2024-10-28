Here is the solution to the problem:

```java
import java.util.*;

class Solution {
    public List<List<Integer>> getRow(List<List<Integer>> lst, int x) {
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            List<Integer> row = lst.get(i);
            for (int j = row.size() - 1; j >= 0; j--) {
                if (row.get(j).equals(x)) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }
        Collections.sort(result, new Comparator<List<Integer>>() {
            public int compare(List<Integer> o1, List<Integer> o2) {
                return o1.get(0).compareTo(o2.get(0));
            }
        });
        return result;
    }
}
```

This solution iterates through each row of the list, and for each row, it iterates through the elements from right to left. If an element is equal to the target value, it adds the coordinate to the result list. After finding all the coordinates, it sorts the result list based on the row index in ascending order. The time complexity is O(n*m), where n is the number of rows and m is the maximum number of columns in a row. The space complexity is O(n*m), where n is the number of rows and m is the maximum number of columns in a row.