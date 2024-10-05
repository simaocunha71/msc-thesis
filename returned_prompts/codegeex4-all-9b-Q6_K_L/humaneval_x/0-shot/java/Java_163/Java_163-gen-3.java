```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> generateIntegers(int a, int b) {
        List<Integer> result = new ArrayList<>();
        for (int i = a; i <= b; i++) {
            if (isEven(i)) {
                result.add(i);
            }
        }
        return result;
    }

    private boolean isEven(int num) {
        while (num > 0) {
            if (num % 2 != 0) {
                return false;
            }
            num /= 10;
        }
        return true;
    }
}
```

Explanation:
The `generateIntegers` method takes two integers `a` and `b` and returns a list of even digits between `a` and `b`. It uses a loop to iterate through all the numbers between `a` and `b` (inclusive) and checks if each number is even by calling the `isEven` method.

The `isEven` method takes an integer `num` and checks if all the digits in `num` are even. It does this by repeatedly dividing `num` by 10 and checking if the remainder when `num` is divided by 2 is not equal to 0. If the remainder is not equal to 0, then `num` is not even and the method returns `false`. If the remainder is equal to 0, then `num` is even and the method returns `true`.