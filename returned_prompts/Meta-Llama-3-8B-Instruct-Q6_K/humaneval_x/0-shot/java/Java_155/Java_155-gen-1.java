Here is a simple Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> evenOddCount(int num) {
        int even = 0, odd = 0;
        
        while(num != 0) {
            int digit = num % 10;
            if(digit % 2 == 0) even++;
            else odd++;
            num /= 10;
        }
        
        List<Integer> result = new ArrayList<>();
        result.add(even);
        result.add(odd);
        return result;
    }
}
```
This solution works by iterating over the digits of the input number from right to left. For each digit, it checks if the digit is even or odd and increments the corresponding counter. Finally, it returns a list containing the counts of even and odd digits. The time complexity of this solution is O(log(n)), where n is the input number, because it processes each digit once. The space complexity is O(1), because it uses a constant amount of space to store the counters and the result list.