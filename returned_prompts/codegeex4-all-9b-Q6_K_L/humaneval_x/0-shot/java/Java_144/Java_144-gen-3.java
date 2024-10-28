Here is a Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean simplify(String x, String n) {
        // Split the input strings into numerator and denominator
        String[] xParts = x.split("/");
        String[] nParts = n.split("/");
        
        // Convert the numerator and denominator from strings to integers
        int xNum = Integer.parseInt(xParts[0]);
        int xDen = Integer.parseInt(xParts[1]);
        int nNum = Integer.parseInt(nParts[0]);
        int nDen = Integer.parseInt(nParts[1]);
        
        // Multiply the numerators and denominators
        int resultNum = xNum * nNum;
        int resultDen = xDen * nDen;
        
        // Check if the result is a whole number
        return resultNum % resultDen == 0;
    }
}
```

This solution splits the input strings into numerator and denominator, converts them into integers, multiplies them, and then checks if the result is a whole number.