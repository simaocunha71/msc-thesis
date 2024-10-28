The problem is asking to find if there are three distinct elements in the list that sum to zero. 

The solution can be achieved by sorting the list and then using three pointers to find three elements that sum to zero.

Here is the Java code to solve the problem:

```java
import java.util.*;

class Solution {
    public boolean triplesSumToZero(List<Integer> l) {
        Collections.sort(l);
        for (int i = 0; i < l.size() - 2; i++) {
            int left = i + 1;
            int right = l.size() - 1;
            while (left < right) {
                int sum = l.get(i) + l.get(left) + l.get(right);
                if (sum < 0) {
                    left++;
                } else if (sum > 0) {
                    right--;
                } else {
                    return true;
                }
            }
        }
        return false;
    }
}
```

This code first sorts the list. Then it uses three pointers: `i`, `left`, and `right`. `i` is used to track the first element, `left` is used to track the second element, and `right` is used to track the third element. The sum of the three elements is calculated and if it is less than zero, `left` is incremented. If the sum is greater than zero, `right` is decremented. If the sum is equal to zero, the function returns `true`. If the loop finishes without finding a triplet that sums to zero, the function returns `false`. 

The time complexity of this solution is O(n^2) where n is the size of the list, because of the two nested loops. The space complexity is O(1) because it only uses a constant amount of space. 