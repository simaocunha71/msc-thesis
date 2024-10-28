Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            if (hasOnlyOddDigits(num)) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }

    private boolean hasOnlyOddDigits(int num) {
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                return false;
            }
            num /= 10;
        }
        return true;
    }
}
```
This solution iterates over the input list and checks each number to see if it has only odd digits. If it does, it adds the number to the result list. After processing all numbers, the solution sorts the result list and returns it.

The `hasOnlyOddDigits` method checks if a number has only odd digits by repeatedly taking the remainder of the number when divided by 10 (to get the last digit), and checking if it's even. If it is, the method returns `false`. If the number becomes 0, it means all digits were odd, so the method returns `true`.

The `uniqueDigits` method uses this helper method to filter out numbers with even digits, and then sorts the result list using the `Collections.sort` method. The resulting list is then returned.