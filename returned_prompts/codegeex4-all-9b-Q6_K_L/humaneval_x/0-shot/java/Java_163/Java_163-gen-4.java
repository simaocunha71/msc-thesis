```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generateIntegers(2, 8) => [2, 4, 6, 8]
    generateIntegers(8, 2) => [2, 4, 6, 8]
    generateIntegers(10, 14) => []
     */
    public List<Integer> generateIntegers(int a, int b) {
        Set<Integer> evenDigits = new HashSet<>();
        for (int i = a; i <= b; i++) {
            int num = i;
            while (num > 0) {
                int digit = num % 10;
                if (digit % 2 == 0) {
                    evenDigits.add(digit);
                }
                num /= 10;
            }
        }
        List<Integer> result = new ArrayList<>(evenDigits);
        Collections.sort(result);
        return result;
    }
}
```