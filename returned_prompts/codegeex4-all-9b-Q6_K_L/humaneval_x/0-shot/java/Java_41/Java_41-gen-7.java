Here is a Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int carRaceCollision(int n) {
        // If n is odd, there will be (n/2) + 1 cars from each direction,
        // and each car from one direction will collide with each car from the other direction
        if (n % 2 == 1) {
            return (n / 2) + 1;
        }
        // If n is even, there will be n/2 cars from each direction,
        // and each car from one direction will collide with each car from the other direction
        else {
            return n / 2;
        }
    }
}
```
This solution is based on the fact that the cars moving in opposite directions will collide with each other. The number of collisions will be equal to the number of cars from each direction, which is `n/2` for both directions. If `n` is odd, there will be one extra car from one direction, which will also collide with each car from the other direction.