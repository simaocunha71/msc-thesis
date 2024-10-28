Here is the Java implementation of the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean simplify(String x, String n) {
        String[] xArr = x.split("/");
        String[] nArr = n.split("/");
        int xNum = Integer.parseInt(xArr[0]);
        int xDen = Integer.parseInt(xArr[1]);
        int nNum = Integer.parseInt(nArr[0]);
        int nDen = Integer.parseInt(nArr[1]);

        return (xNum * nDen) % (xDen * nNum) == 0;
    }
}
```

This function splits the input strings by '/' and parses them into integers. Then it calculates the product of the numerators and denominators of both fractions and checks if the result is divisible by the other fraction. If it is, the function returns true, otherwise it returns false.