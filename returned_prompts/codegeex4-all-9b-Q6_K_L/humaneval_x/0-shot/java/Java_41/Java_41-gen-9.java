The number of collisions that will occur in this car race is given by the formula:

\[
\text{collisions} = \frac{n(n-1)}{2}
\]

This formula is derived from the fact that each car moving left to right can potentially collide with each car moving right to left. Since there are \( n \) cars in each direction, there are a total of \( n \times n \) possible collisions. However, since each collision involves a car moving left to right and a car moving right to left, the total number of collisions is reduced by half, resulting in the formula above.

Here is the Java implementation of the function:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int carRaceCollision(int n) {
        return n * (n - 1) / 2;
    }
}
```