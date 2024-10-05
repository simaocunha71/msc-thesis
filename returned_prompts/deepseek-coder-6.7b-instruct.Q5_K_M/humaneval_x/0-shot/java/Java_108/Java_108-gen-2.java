        int count = 0;
        for (int num : arr) {
            int sum = 0;
            if (num < 0) {
                String strNum = String.valueOf(num);
                for (int i = 1; i < strNum.length(); i++) {
                    sum += Character.getNumericValue(strNum.charAt(i));
                }
                if (sum > 0) {
                    count++;
                }
            } else {
                String strNum = String.valueOf(num);
                for (int i = 0; i < strNum.length(); i++) {
                    sum += Character.getNumericValue(strNum.charAt(i));
                }
                if (sum > 0) {
                    count++;
                }
            }
        }
        return count;
    }
}


A: Here is a correct answer:
```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function countNums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> countNums(Arrays.asList()) 
    0
    >>> countNums(Arrays.asList(-1, 11, -11)) 
    1
    >>> countNums(Arrays.asList(1, 1, 2)) 
    3
      */
    public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
            int sum = 0;
            String strNum = String.valueOf(num);
            for (int i = 0; i < strNum.length(); i++) {
                sum += Character.getNumericValue(strNum.charAt(i));
            }
            if (sum > 0) {
                count++;
            }
        }
        return count;
    }
}
```
The function first converts the numbers to