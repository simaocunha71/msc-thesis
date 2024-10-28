Here is the solution for the problem:

```java
import java.util.*;

class Solution {
    /**
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circularShift(12, 1)
    "21"
    >>> circularShift(12, 2)
    "12"
     */
    public String circularShift(int x, int shift) {
        // Convert integer to string
        String s = String.valueOf(x);
        
        // Calculate the actual shift
        shift = shift % s.length();
        
        // Perform the circular shift
        String result = s.substring(shift) + s.substring(0, shift);
        
        return result;
    }
}
```

This solution works by first converting the integer to a string. Then, it calculates the actual shift by taking the modulus of the shift with the length of the string. This is because if the shift is greater than the number of digits, it is equivalent to shifting the digits by the remainder of the shift divided by the number of digits.

Then, it uses the `substring` method to extract the part of the string that should be at the end of the result and the part that should be at the beginning of the result, and concatenates them to form the final result.

The time complexity of this solution is O(n), where n is the number of digits in the integer, because it involves a constant amount of work for each digit. The space complexity is also O(n), because it needs to store the result string.