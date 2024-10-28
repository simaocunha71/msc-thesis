Here is a Java solution to the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            if (!hasEvenDigit(num)) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }

    private boolean hasEvenDigit(int num) {
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                return true;
            }
            num /= 10;
        }
        return false;
    }
}
```

This solution works by iterating over each number in the input list and checking if it has any even digits. If a number does not have any even digits, it is added to the result list. After all numbers have been processed, the result list is sorted and returned.

The `hasEvenDigit` method checks if a number has any even digits by repeatedly taking the remainder of the number when divided by 10 (which gives the last digit of the number), checking if the digit is even, and then removing the last digit from the number. If any even digit is found, the method returns `true`; otherwise, it returns `false`.