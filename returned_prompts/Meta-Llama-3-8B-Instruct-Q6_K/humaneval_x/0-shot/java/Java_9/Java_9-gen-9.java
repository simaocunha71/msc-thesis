    import java.util.*;

    public class Solution {
        public List<Integer> rollingMax(List<Integer> numbers) {
            List<Integer> result = new ArrayList<>();
            int max = Integer.MIN_VALUE;

            for (int num : numbers) {
                result.add(Math.max(num, max));
                max = Math.max(num, max);
            }

            return result;
        }
    }
    
    Explanation:
    The rollingMax function takes a list of integers as input and returns a new list where each element is the maximum value seen so far in the input list. It maintains a running maximum value and updates it whenever it encounters a larger value. It adds the current maximum value to the result list and updates the running maximum value for the next iteration. The function returns the result list at the end. In the given example, the function returns [1, 2, 3, 3, 3, 4, 4] which is the list of rolling maximum elements found until each given moment in the sequence. .


