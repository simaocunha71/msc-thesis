Here is the Java code that solves the problem:

```java
import java.util.*;

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

This code iterates through each row in the list, checks if the current element is equal to `x`, and if it is, adds the coordinates of the element to the result list. After all elements have been checked, the result list is sorted based on the row and column indices. The sorting is done by first comparing the row indices, and if they are equal, then comparing the column indices. The sorted list is then returned. 

For example, given the list `[[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]]` and the integer `1`, the function will return `[[0, 0], [1, 4], [1, 0], [2, 5], [2, 0]]`. If the list is empty or `x` is not found in the list, the function will return an empty list. 