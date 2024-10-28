```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        int size = lst.size();
        List<Integer> result = new ArrayList<>(size);
        if (size == 0) return result;

        int[] arr = lst.stream().mapToInt(Integer::intValue).toArray();
        int left = 0, right = size - 1, turn = 0;
        while (left <= right) {
            if (turn % 2 == 0) {
                result.add(arr[left]);
                left++;
            } else {
                result.add(arr[right]);
                right--;
            }
            turn++;
        }
        return result;
    }
}
```