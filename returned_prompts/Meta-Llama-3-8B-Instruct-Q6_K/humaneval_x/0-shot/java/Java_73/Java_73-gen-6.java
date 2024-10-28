This problem can be solved by comparing each element in the array with its corresponding element from the end of the array. If the elements are not equal, then the element needs to be changed to make the array palindromic. We can keep track of the count of elements that need to be changed.

Here is the Java code that implements this solution:

```java
import java.util.*;

class Solution {
    public int smallestChange(List<Integer> arr) {
        int count = 0;
        int left = 0;
        int right = arr.size() - 1;
        while (left < right) {
            if (!arr.get(left).equals(arr.get(right))) {
                count++;
                right--;
            } else {
                left++;
            }
        }
        return count;
    }
}
```

In this code, we initialize two pointers, `left` and `right`, to the start and end of the array respectively. We then enter a while loop that continues until `left` is no longer less than `right`. Inside the loop, we check if the elements at the `left` and `right` indices are equal. If they are not equal, we increment the count of elements that need to be changed and decrement `right`. If they are equal, we increment `left`. At the end of the loop, `count` will hold the minimum number of elements that need to be changed to make the array palindromic. We return this count.