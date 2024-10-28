```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean rightAngleTriangle(int a, int b, int c) {
        if (a <= 0 || b <= 0 || c <= 0) {
            return false;
        }
        int[] sides = {a, b, c};
        Arrays.sort(sides);
        return sides[0] * sides[0] + sides[1] * sides[1] == sides[2] * sides[2];
    }
}
```