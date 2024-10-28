```java
import java.util.*;
import java.lang.*;

class Solution {
    public int carRaceCollision(int n) {
        // We can use the formula n*(n+1)/2 to calculate the number of collisions.
        // This formula is derived from the fact that there are n*(n+1)/2 pairs of cars
        // that can potentially collide.  Each pair of cars has a 50% chance of colliding,
        // so the total number of collisions is n*(n+1)/2 * 0.5 = n*(n+1)/4.
        return n * (n + 1) / 4;
    }
}
```