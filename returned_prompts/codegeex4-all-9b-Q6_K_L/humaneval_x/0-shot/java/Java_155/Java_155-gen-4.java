```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given an integer. return a tuple that has the number of even and odd digits respectively.
    
     Example:
        evenOddCount(-12) ==> (1, 1)
        evenOddCount(123) ==> (1, 2)
     */
    public List<Integer> evenOddCount(int num) {
        List<Integer> result = new ArrayList<>();
        int evenCount = 0, oddCount = 0;
        String str = Integer.toString(Math.abs(num));
        for (int i = 0; i < str.length(); i++) {
            int digit = str.charAt(i) - '0';
            if (digit % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }
        result.add(evenCount);
        result.add(oddCount);
        return result;
    }
}
```

Explanation:
1. We start by creating a `List<Integer>` called `result` to store the even and odd counts.
2. We initialize `evenCount` and `oddCount` to 0.
3. We convert the input number to a string using `Integer.toString(Math.abs(num))` to handle negative numbers.
4. We iterate through each character in the string and convert it to an integer using `str.charAt(i) - '0'`.
5. If the digit is even (i.e., divisible by 2), we increment `evenCount`. Otherwise, we increment `oddCount`.
6. Finally, we add `evenCount` and `oddCount` to the `result` list and return it.