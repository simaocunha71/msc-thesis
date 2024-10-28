Here is a Java solution that meets the requirements:

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

This solution iterates over each row in the list, and for each row, it iterates over each element in reverse order. If it finds the element `x`, it adds its coordinates to the result list. Finally, it sorts the result list by the row index in ascending order.

The time complexity of this solution is O(n*m), where n is the number of rows and m is the maximum number of columns. The space complexity is O(k), where k is the number of occurrences of `x` in the list. If `x` is not found in the list, the result list will be empty. If `x` is found multiple times in the same row, the coordinates will be added to the result list in reverse order of the column indices. If `x` is not found in the list, the result list will be empty. If `x` is found in multiple rows, the coordinates will be added to the result list in ascending order of the row indices.

The test cases provided in the problem description are all handled correctly by this solution. For example, `getRow([[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]], 1)` returns `[[0, 0], [1, 4], [1, 0], [2, 5], [2, 0]]`, which is the expected result. Similarly, `getRow([], 1)` returns an empty list, which is the expected result. `getRow([[1], [1, 2, 3]], 3)` returns `[[1, 2]]`, which is the expected result. `getRow([[], [1], [1