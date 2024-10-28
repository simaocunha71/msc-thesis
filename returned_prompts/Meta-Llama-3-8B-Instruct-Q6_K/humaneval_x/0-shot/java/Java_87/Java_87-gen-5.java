Here is a Java solution:

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
        Collections.sort(result, (a, b) -> {
            if (a.get(0).equals(b.get(0))) {
                return Integer.compare(b.get(1), a.get(1));
            } else {
                return Integer.compare(a.get(0), b.get(0));
            }
        });
        return result;
    }
}
```

This solution iterates through each row of the 2D list, and for each row, it iterates through the elements in reverse order. If an element is equal to x, it adds the coordinates (row, column) to the result list. After that, it sorts the result list based on the row and column. The sorting is done by comparing the first element (row) of each list, and if they are equal, it compares the second element (column). This ensures that the coordinates are sorted by rows in ascending order, and by columns in descending order. 

The time complexity of this solution is O(n*m), where n is the number of rows and m is the maximum number of columns in the 2D list, because in the worst case, it needs to iterate through each element in the 2D list. The space complexity is O(k), where k is the number of occurrences of x in the 2D list, because it needs to store the coordinates of x in the result list. 