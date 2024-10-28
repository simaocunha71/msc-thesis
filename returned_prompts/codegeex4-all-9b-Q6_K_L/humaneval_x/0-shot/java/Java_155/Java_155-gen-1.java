Here is the Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> evenOddCount(int num) {
        int countEven = 0, countOdd = 0;
        String strNum = Math.abs(num) + "";
        for (char digit : strNum.toCharArray()) {
            if (Character.isDigit(digit)) {
                int value = Character.getNumericValue(digit);
                if (value % 2 == 0) {
                    countEven++;
                } else {
                    countOdd++;
                }
            }
        }
        return Arrays.asList(countEven, countOdd);
    }
}
```
In the above code, we first convert the integer to its absolute value and then convert it to a string. Then we iterate through each character in the string. If the character is a digit, we convert it to an integer and check if it's even or odd. We increment the corresponding count variable accordingly. Finally, we return a list containing the counts of even and odd digits.

The time complexity of this solution is O(d), where d is the number of digits in the input number.