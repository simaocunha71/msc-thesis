Here is the Java code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> evenOddCount(int num) {
        int evenCount = 0;
        int oddCount = 0;
        String strNum = String.valueOf(Math.abs(num)); // convert to absolute value and string
        for (int i = 0; i < strNum.length(); i++) {
            int digit = Character.getNumericValue(strNum.charAt(i));
            if (digit % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }
        return Arrays.asList(evenCount, oddCount);
    }
}
```

This code first converts the input number to a string and then iterates through the characters of the string. For each character, it converts it back to a number and checks if it is even or odd, incrementing the respective counter. Finally, it returns a list containing the counts of even and odd digits.