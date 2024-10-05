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
        result.sort((a, b) -> Integer.compare(a.get(0), b.get(0)));
        return result;
    }
}
```
The solution iterates over each row in the list and checks each element in the row to see if it is equal to the given integer `x`. If it is, the row and column indices are added to the result list. After all elements have been checked, the result list is sorted by the row index in ascending order. 

The sorting is done using the `sort` method of the `List` interface, which takes a comparator as an argument. The comparator is a lambda expression that compares two lists of integers by their first element (the row index). The `compare` method of the `Integer` class is used to compare the row indices. 

The time complexity of this solution is O(n*m), where n is the number of rows in the list and m is the maximum number of columns in a row. The space complexity is O(k), where k is the number of occurrences of `x` in the list. 

The solution returns a list of lists, where each inner list contains the row and column indices of an occurrence of `x` in the list. The inner lists are sorted by the row indices in ascending order. 

For example, if the input list is `[[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]]` and the integer `x` is `1`, the output will be `[[0, 0], [1, 4], [1, 0], [2, 5], [2, 0]]`. If the input list is `[]` and the integer `x` is `1`, the output will be an empty list. If the input list is `[[1], [1, 2