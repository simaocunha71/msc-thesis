    import java.util.*;

    public class Solution {
        public List<Integer> removeDuplicates(List<Integer> numbers) {
            Map<Integer, Boolean> map = new HashMap<>();
            List<Integer> result = new ArrayList<>();

            for (Integer number : numbers) {
                if (!map.containsKey(number)) {
                    map.put(number, true);
                    result.add(number);
                }
            }

            return result;
        }
    }

    // Testing the method
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> numbers = Arrays.asList(1, 2, 3, 2, 4);
        List<Integer> result = solution.removeDuplicates(numbers);
        System.out.println(result); // Output: [1, 3, 4]
    }
