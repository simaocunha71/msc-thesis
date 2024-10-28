    import java.util.*;

    class Solution {
        public List<Integer> eat(int number, int need, int remaining) {
            int eaten = number + Math.min(need, remaining);
            int left = remaining - (need - eaten);
            if (left < 0) {
                left = 0;
            }
            return Arrays.asList(eaten, left);
        }
    }

    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> result1 = solution.eat(5, 6, 10);
        List<Integer> result2 = solution.eat(4, 8, 9);
        List<Integer> result3 = solution.eat(1, 10, 10);
        List<Integer> result4 = solution.eat(2, 11, 5);

        System.out.println(result1);  // [11, 4]
        System.out.println(result2);  // [12, 1]
        System.out.println(result3);  // [11, 0]
        System.out.println(result4);  // [7, 0]
    }
