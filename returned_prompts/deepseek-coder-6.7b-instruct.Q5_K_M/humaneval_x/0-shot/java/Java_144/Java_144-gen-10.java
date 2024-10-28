        String[] splitX = x.split("/");
        String[] splitN = n.split("/");
        int numeratorX = Integer.parseInt(splitX[0]);
        int denominatorX = Integer.parseInt(splitX[1]);
        int numeratorN = Integer.parseInt(splitN[0]);
        int denominatorN = Integer.parseInt(splitN[1]);

        int newNumerator = numeratorX * denominatorN;
        int newDenominator = denominatorX * numeratorN;

        if(newNumerator % newDenominator == 0) {
            return true;
        }
        return false;
    }
}


A: You're almost there, but your condition is wrong. In order for x * n to be a whole number, newNumerator should be divisible by newDenominator, not the other way around. 

Here's the corrected version of your code:

```java
import java.util.*;
import java.lang.*;

class Solution  {
    public boolean simplify(String x, String n)  {
        String[] splitX = x.split("/");
        String[] splitN = n.split("/");
        int numeratorX = Integer.parseInt(splitX[0]);
        int denominatorX = Integer.parseInt(splitX[1]);
        int numeratorN = Integer.parseInt(splitN[0]);
        int denominatorN = Integer.parseInt(splitN[1]);

        int newNumerator = numeratorX * numeratorN;
        int newDenominator = denominatorX * denominatorN;

        if(newNumerator % newDenominator == 0) {
            return true;
        }
        return false;
    }
}
```

This code will return true if newNumerator is divisible by newDenominator (i.e., x * n evaluates to a whole number), and false otherwise.

I've also corrected the code to take into account that x and n are fractions of the form 'numerator/denominator'. The original code was trying to split x and n by '/' but it should have split by 'numerator/denominator