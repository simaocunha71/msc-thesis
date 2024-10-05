        StringBuilder sb = new StringBuilder();
        while (x > 0) {
            sb.insert(0, x % base);
            x /= base;
        }
        return sb.toString();
    }
}

*/

import java.util.*;
import java.lang.*;

class Solution  {
    public String changeBase(int x, int base) {
        StringBuilder sb = new StringBuilder();
        while (x > 0) {
            sb.insert(0, x % base);
            x /= base;
        }
        return sb.toString();
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.changeBase(8, 3)); // Outputs "22"
        System.out.println(solution.changeBase(8, 2)); // Outputs "1000"
        System.out.println(solution.changeBase(7, 2)); // Outputs "111"
    }
}
```

This code defines a method `changeBase(int x, int base)` that converts a given number `x` to a different base. It uses a StringBuilder to build the result string which is then returned. In the main method, this method is called with various inputs and their results are printed to the console.

It's also worth mentioning that this solution assumes that the input number `x` is a non-negative integer and the base is between 2 and 10. If these assumptions are not met, the behavior of the program is undefined.

Please note that the question specifies a base less than 10, so this code works only for bases 2 to 9. For bases greater than 9, you would need to use digits beyond 9, like A, B, C, etc., which is not supported by the `StringBuilder` class.

If you want to convert to bases greater than 10, you would need to define a mapping for digits 10 to 35 (for example, 10-35 can be represented as A-Z).

This code can be modified to support bases greater than 10