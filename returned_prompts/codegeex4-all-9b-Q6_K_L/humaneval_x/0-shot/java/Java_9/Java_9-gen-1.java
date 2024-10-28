Here is a possible solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> rollingMax(List<Integer> numbers) {
        List<Integer> maxes = new ArrayList<Integer>();
        int max = Integer.MIN_VALUE;
        for(int i = 0; i < numbers.size(); i++) {
            if(numbers.get(i) > max) {
                max = numbers.get(i);
            }
            maxes.add(max);
        }
        return maxes;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<Integer> numbers = Arrays.asList(1, 2, 3, 2, 3, 4, 2);
        List<Integer> maxes = s.rollingMax(numbers);
        System.out.println(maxes);
    }
}
```

This program creates a new list `maxes` to store the rolling maximums. It then iterates through the input list `numbers`, updating `max` to the current number if it's greater than `max`, and adding `max` to `maxes`. Finally, it returns `maxes`.

The `main` method demonstrates how to use this function with a sample list of numbers.