Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public boolean isSorted(List<Integer> lst) {
        if (lst.size() == 0) {
            return true;
        }
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
The solution iterates through the list of integers, checking if each element is less than the previous one. If it finds two consecutive elements that are not in ascending order, it immediately returns `false`. If it reaches the end of the list without finding any duplicates, it returns `true`.

Note: The solution assumes that the list contains only positive integers, as specified in the problem statement. If the list can contain negative numbers or non-integer values, additional checks would be needed. Also, the solution does not handle the case where the list is empty, but since the problem statement mentions a list of numbers, I assume that the list will always contain at least one element. If the list can be empty, the solution should return `true` in that case.