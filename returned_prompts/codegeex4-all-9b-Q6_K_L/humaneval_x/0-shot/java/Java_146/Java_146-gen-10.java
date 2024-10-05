```java
import java.util.*;
import java.lang.*;

class Solution {
    public int specialFilter(List<Integer> nums) {
        return (int) nums.stream()
                .filter(num -> num > 10 && isOdd(num) && isOddFirstAndLast(num))
                .count();
    }

    private boolean isOdd(int num) {
        return num % 2 != 0;
    }

    private boolean isOddFirstAndLast(int num) {
        int firstDigit = num;
        while (firstDigit >= 10) {
            firstDigit /= 10;
        }
        int lastDigit = num % 10;
        return isOdd(firstDigit) && isOdd(lastDigit);
    }
}
```