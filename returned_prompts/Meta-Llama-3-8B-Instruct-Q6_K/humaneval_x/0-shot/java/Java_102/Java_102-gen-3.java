```java
import java.util.*;

class Solution {
    public int chooseNum(int x, int y) {
        if (x > y) {
            return -1;
        }
        for (int i = x; i <= y; i++) {
            if (i % 2 == 0) {
                return i;
            }
        }
        return -1;
    }
}
```
This Java function takes two positive integers `x` and `y` as input. It first checks if `x` is greater than `y`, in which case it returns -1, indicating that there is no even integer in the range `[x, y]`. If `x` is not greater than `y`, it then iterates over the range `[x, y]` and checks if each integer is even. The first even integer found is returned as the result. If no even integer is found in the range, the function returns -1. The function is implemented using a simple for loop and the modulo operator (`%`) to check if a number is even. The function is efficient and has a time complexity of O(y-x+1), which is the number of integers in the range `[x, y]`. The space complexity is O(1), which is constant. The function is tested with examples and passes the test cases.