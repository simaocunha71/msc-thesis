        if (n > m){
            return -1;
        }
        else {
            int avg = (n + m) / 2;
            double roundedAvg = Math.round(avg);
            String binary = Integer.toBinaryString((int) roundedAvg);
            return binary;
        }
    }
}


A: Your code is correct. The only thing you should consider is the data type of the return value. In this case, the return value is a binary string of a rounded average of two integers.

In Java, the Integer.toBinaryString method returns a String representation of the integer argument as a binary (base 2) number. The returned String always represent a number without a sign, so the argument must be a positive integer or zero.

So, your method should return a String type.

The other thing is, if n is greater than m, your method should return -1 which is an integer type.

So, the correct answer should be:

```java
import java.util.*;
import java.lang.*;

class Solution  {
    public Object roundedAvg(int n, int m)  {
        if (n > m){
            return -1;
        }
        else {
            int avg = (n + m) / 2;
            double roundedAvg = Math.round(avg);
            String binary = Integer.toBinaryString((int) roundedAvg);
            return binary;
        }
    }
}
```

This solution rounds the average of two integers to the nearest integer, converts the rounded average to binary, and returns the binary string. If n is greater than m, it returns -1.

This solution is correct and efficient.


A: Here's a more concise version of your code:

```java
class Solution {
    public String roundedAvg(int n, int m) {
        return n > m ? "-1" : Integer.toBinaryString((n + m) / 2);
    }
}
```

This version of the code uses a ternary operator to check if `n` is greater than `m`. If true, it returns `-1` as a String. If false, it calculates