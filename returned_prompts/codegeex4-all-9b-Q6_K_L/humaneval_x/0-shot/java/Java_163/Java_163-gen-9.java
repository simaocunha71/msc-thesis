```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> generateIntegers(int a, int b) {
        List<Integer> list = new ArrayList<>();
        for (int i = a; i <= b; i++) {
            if (i % 2 == 0 && isEvenDigit(i)) {
                list.add(i);
            }
        }
        return list;
    }

    private boolean isEvenDigit(int num) {
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 != 0) {
                return false;
            }
            num /= 10;
        }
        return true;
    }
}
```