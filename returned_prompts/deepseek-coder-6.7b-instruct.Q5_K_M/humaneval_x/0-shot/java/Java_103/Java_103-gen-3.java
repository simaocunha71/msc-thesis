        if(n > m) {
            return -1;
        }

        double avg = (double)(n + m) / 2;
        int roundedAvg = (int)Math.round(avg);

        return Integer.toBinaryString(roundedAvg);
    }
}


A: You are on the right track, but you should convert the average to an integer before converting it to binary. The rounding operation is not needed if you're calculating the average and want the result to be an integer. 
Here's the corrected code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Object roundedAvg(int n, int m) {
        if(n > m) {
            return -1;
        }

        int avg = (n + m) / 2;

        return Integer.toBinaryString(avg);
    }
}
```

In this corrected code, the average is calculated by adding the two numbers and dividing by 2, then the result is converted to binary by using the Integer.toBinaryString method. If n is greater than m, the method returns -1.

I hope this helps you understand how to solve your problem. If you have any more questions, feel free to ask.


A: You are on the right track, but you should convert the average to an integer before converting it to binary. The rounding operation is not needed if you're calculating the average and want the result to be an integer.

Here's the corrected code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Object roundedAvg(int n, int m) {
        if(n > m) {
            return -1;
        }

        int avg = (n + m) / 2;

        return Integer.toBinaryString(avg);
    }
}
```

In this corrected code, the average is calculated by adding the two numbers and dividing by 2, then the result is converted to binary by using the Integer.toBinaryString method. If n is greater than m, the method returns -1.

I hope this helps you understand