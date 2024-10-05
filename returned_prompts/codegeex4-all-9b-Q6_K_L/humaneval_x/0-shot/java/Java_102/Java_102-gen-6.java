The code you provided has the correct logic for solving the problem. However, there are a few issues that need to be addressed:

1. The function name `chooseNum` is not descriptive. It should be changed to something that clearly indicates its purpose, such as `findBiggestEvenNumberInRange`.

2. The function should be declared as `static` if it's not going to be used outside of the `Solution` class.

3. The function should be declared as `public` if it's going to be used outside of the `Solution` class.

Here's the corrected code:

```java
import java.util.*;
import java.lang.*;

public class Solution {
    public static int findBiggestEvenNumberInRange(int x, int y) {
        if (x > y) {
            return -1;
        }
        
        if (x % 2 != 0) {
            x++;
        }
        
        if (x > y) {
            return -1;
        }
        
        return x;
    }
}
```

This code checks if `x` is greater than `y`, and if so, returns `-1`. If `x` is not greater than `y`, it checks if `x` is odd, and if so, increments `x` by `1`. It then checks if `x` is greater than `y`, and if so, returns `-1`. Finally, it returns `x`, which is the biggest even number in the range `[x, y]`.