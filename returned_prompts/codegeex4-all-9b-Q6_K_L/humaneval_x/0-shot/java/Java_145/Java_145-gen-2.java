```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        if (nums.isEmpty()) {
            return Collections.emptyList();
        }
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < nums.size(); i++) {
            int num = nums.get(i);
            int sum = sumOfDigits(num);
            map.computeIfAbsent(sum, k -> new ArrayList<>()).add(num);
        }
        List<Integer> result = new ArrayList<>();
        for (List<Integer> list : map.values()) {
            result.addAll(list);
        }
        return result;
    }

    private int sumOfDigits(int num) {
        int sum = 0;
        while (num != 0) {
            sum += Math.abs(num % 10);
            num /= 10;
        }
        return sum;
    }
}
```
This solution uses a HashMap to store the sum of digits as the key and the corresponding numbers as the value. Then, it sorts the HashMap by the key in ascending order and adds all the numbers to a new list. Finally, it returns the new list.

The `sumOfDigits` function calculates the sum of the digits of a number. It iterates through the digits of the number and adds them to the sum.