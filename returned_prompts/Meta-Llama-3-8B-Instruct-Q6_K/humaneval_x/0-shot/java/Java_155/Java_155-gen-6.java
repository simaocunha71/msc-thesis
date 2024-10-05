```java
import java.util.*;

class Solution {
    public List<Integer> evenOddCount(int num) {
        int countEven = 0, countOdd = 0;
        while (num != 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                countEven++;
            } else {
                countOdd++;
            }
            num /= 10;
        }
        List<Integer> result = new ArrayList<>();
        result.add(countEven);
        result.add(countOdd);
        return result;
    }
}
```
The code uses a while loop to extract each digit from the input number. It checks if the digit is even (i.e., `digit % 2 == 0`) and increments the corresponding count (`countEven` for even or `countOdd` for odd). After processing all digits, it creates a list with the counts and returns it. The `ArrayList` class from the `java.util` package is used to store the counts. The `add` method is used to add each count to the list. The list is then returned as the result.