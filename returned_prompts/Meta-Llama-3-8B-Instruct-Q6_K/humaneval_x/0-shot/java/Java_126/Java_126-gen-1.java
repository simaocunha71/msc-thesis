```java
import java.util.*;

class Solution {
    public boolean isSorted(List<Integer> lst) {
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i - 1) >= lst.get(i)) {
                return false;
            }
        }
        return true;
    }
}
```

Explanation: 
This solution iterates through the list of integers from the second element to the end. For each element, it checks if the current element is less than or equal to the previous element. If it finds any element that is not less than the previous one, it immediately returns `false`, indicating that the list is not sorted. If it checks all elements without finding any that are not less than the previous one, it returns `true`, indicating that the list is sorted. 

The condition `lst.get(i - 1) >= lst.get(i)` is used to check if the current element is not less than the previous one. If it is greater than or equal to the previous one, it means the list is not sorted, so the function returns `false`. If it is less than the previous one, it means the list is still sorted, so the function continues to the next iteration. 

This solution has a time complexity of O(n), where n is the size of the input list, because it iterates through the list once. The space complexity is O(1), because it uses a constant amount of space to store the loop variable and the comparison result. 