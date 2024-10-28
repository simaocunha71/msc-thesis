Here is a way to solve this problem using Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean simplify(String x, String n) {
        // Split the string into numerator and denominator
        String[] partsX = x.split("/");
        String[] partsN = n.split("/");

        // Convert the strings into integers
        int numeratorX = Integer.parseInt(partsX[0]);
        int denominatorX = Integer.parseInt(partsX[1]);
        int numeratorN = Integer.parseInt(partsN[0]);
        int denominatorN = Integer.parseInt(partsN[1]);

        // Multiply the numerators and denominators
        int numeratorResult = numeratorX * numeratorN;
        int denominatorResult = denominatorX * denominatorN;

        // Check if the result is a whole number
        return numeratorResult % denominatorResult == 0;
    }
}
```

In this code, we first split the input strings into numerators and denominators. Then, we convert these strings into integers. We multiply the numerators and denominators and check if the result is a whole number by checking if the remainder of the division is 0. If it is, we return true; otherwise, we return false.