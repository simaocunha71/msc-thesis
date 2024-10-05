The task is to find all integers in the given list that do not have any even digits. Then, return the list in sorted order.

Here's a Java solution for this problem:

```java
import java.util.*;

class Solution {
    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            boolean hasEvenDigit = false;
            int temp = num;
            while (temp != 0) {
                int digit = temp % 10;
                if (digit % 2 == 0) {
                    hasEvenDigit = true;
                    break;
                }
                temp /= 10;
            }
            if (!hasEvenDigit) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }
}
```

This solution iterates over each number in the list. For each number, it checks if any digit is even. If no even digit is found, the number is added to the result list. Finally, the result list is sorted and returned. 

For example, if the input list is [15, 33, 1422, 1], the output will be [1, 15, 33]. If the input list is [152, 323, 1422, 10], the output will be an empty list because all numbers in the input list have at least one even digit. 