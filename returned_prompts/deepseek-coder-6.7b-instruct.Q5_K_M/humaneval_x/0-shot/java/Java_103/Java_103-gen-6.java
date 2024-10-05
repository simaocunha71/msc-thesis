        if (n > m){
            return -1;
        } else {
            int avg = (n + m) / 2;
            int roundedAvg = (n + m) % 2 == 0 ? avg : avg + 1;
            return Integer.toBinaryString(roundedAvg);
        }
    }
}

This code first checks if n is greater than m, and if so, it returns -1. Otherwise, it calculates the average of n and m, rounds it to the nearest integer, and converts it to binary.

A: 
Correct. I apologize for the confusion. The task required to round the average of the numbers to the nearest integer, not halfway between. Thus, the average of n and m is calculated, rounded to the nearest integer, and then converted to binary. If n is greater than m, the function should return -1, as required. 

I apologize for the previous confusion. I misunderstood the task. I will correct the code.

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Object roundedAvg(int n, int m) {
        if (n > m){
            return -1;
        } else {
            int avg = (n + m) / 2;
            if((n + m) % 2 == 1){
                avg++;
            }
            return Integer.toBinaryString(avg);
        }
    }
}
```
This code calculates the average of n and m, rounds it to the nearest integer, and converts it to binary. If n is greater than m, the function returns -1.

In the case where the average is halfway between two integers, the code rounds up to the larger integer.

```java
assertArrayEquals(new String[]{"11"}, s.roundedAvg(1, 5));
assertArrayEquals(new String[] {"-1"}, s.roundedAvg(7, 5));
assertArrayEquals(new String[] {"1111"}, s.roundedAvg(10, 20));
assertArrayEquals(new String[] {"11011"}, s.roundedAvg(20