Here is the solution for the problem:

```java
import java.util.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<String> result = new ArrayList<>();
        for (Integer num : arr) {
            if (num >= 1 && num <= 9) {
                result.add(getName(num));
            }
        }
        Collections.sort(result);
        Collections.reverse(result);
        return result;
    }

    private String getName(int num) {
        String[] names = {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        return names[num - 1];
    }
}
```

Explanation:

1. We iterate over the input array and filter out the numbers between 1 and 9 inclusive. For each of these numbers, we call the `getName` method to get the corresponding name.
2. We sort the resulting list of names in ascending order.
3. We reverse the sorted list to get the desired output.
4. The `getName` method simply returns the name corresponding to the given number by indexing into the `names` array.

Note: This solution assumes that the input array does not contain any numbers outside the range 1-9. If the input array can contain such numbers, we should add additional logic to handle them. For example, we could ignore them or replace them with a special value like "Invalid".