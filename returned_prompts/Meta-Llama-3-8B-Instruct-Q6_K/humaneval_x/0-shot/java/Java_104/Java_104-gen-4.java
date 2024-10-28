Here is the Java code to solve the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            boolean hasEvenDigit = false;
            for (char c : String.valueOf(num).toCharArray()) {
                if (Integer.parseInt(String.valueOf(c)) % 2 == 0) {
                    hasEvenDigit = true;
                    break;
                }
            }
            if (!hasEvenDigit) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }
}
```

This code first iterates over each number in the input list. For each number, it checks if any of its digits is even. If it finds a number with no even digits, it adds it to the result list. After processing all numbers, it sorts the result list in increasing order and returns it. The time complexity of this code is O(n*m), where n is the number of elements in the input list and m is the maximum number of digits in a number. The space complexity is O(n), as we need to store the result in a list.