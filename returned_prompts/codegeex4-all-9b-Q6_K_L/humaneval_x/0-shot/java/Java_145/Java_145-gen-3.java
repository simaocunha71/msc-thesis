```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> orderByPoints(List<Integer> nums) {
        Map<Integer, List<Integer>> digitSumToNums = new HashMap<>();
        for (int i = 0; i < nums.size(); i++) {
            int num = nums.get(i);
            int digitSum = 0;
            while (num != 0) {
                digitSum += Math.abs(num % 10);
                num /= 10;
            }
            if (!digitSumToNums.containsKey(digitSum)) {
                digitSumToNums.put(digitSum, new ArrayList<>());
            }
            digitSumToNums.get(digitSum).add(nums.get(i));
        }
        List<Integer> result = new ArrayList<>();
        List<Integer> digitSums = new ArrayList<>(digitSumToNums.keySet());
        Collections.sort(digitSums);
        for (int digitSum : digitSums) {
            List<Integer> numsWithDigitSum = digitSumToNums.get(digitSum);
            Collections.sort(numsWithDigitSum);
            result.addAll(numsWithDigitSum);
        }
        return result;
    }
}
```