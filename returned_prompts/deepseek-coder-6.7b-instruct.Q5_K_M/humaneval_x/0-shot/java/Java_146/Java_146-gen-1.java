        int count = 0;
        for (int num : nums) {
            if (num > 10) {
                int firstDigit = Math.abs(num);
                while (firstDigit >= 10) {
                    firstDigit /= 10;
                }
                int lastDigit = num % 10;
                if (firstDigit % 2 != 0 && lastDigit % 2 != 0) {
                    count++;
                }
            }
        }
        return count;
    }
}

```

## Answer Key
```java
import java.util.*;
import java.lang.*;

class Solution  {
    public int specialFilter(List<Integer> nums) {
        int count = 0;
        for (int num : nums) {
            if (num > 10) {
                int firstDigit = Math.abs(num);
                while (firstDigit >= 10) {
                    firstDigit /= 10;
                }
                int lastDigit = num % 10;
                if (firstDigit % 2 != 0 && lastDigit % 2 != 0) {
                    count++;
                }
            }
        }
        return count;
    }
}
```

## Explanation
The provided code is a solution to the problem. It loops through each element in the input list and checks whether it meets the conditions specified in the problem statement. If the number is greater than 10 and both the first and last digits are odd (1, 3, 5, 7, or 9), it increments a counter. Finally, it returns the count of such numbers.

It is important to note that the first digit of a number is calculated by taking the absolute value of the number and then repeatedly dividing by 10 until we reach a number less than 10, which is the first digit. The last digit of a number is calculated by taking the modulus of the number by 10.

The conditions for the first and last digits to be odd are checked using the modulus operator (%). If the remainder of dividing the digit by 2 is not 0, then the digit is odd.

