import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    willItFly(Arrays.asList(1, 2), 5) -> false
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    willItFly(Arrays.asList(3, 2, 3), 1) -> false
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    willItFly(Arrays.asList(3, 2, 3), 9) -> true
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    willItFly(Arrays.asList(3), 5) -> true
    # 3 is less than the maximum possible weight, and it's balanced.
     */
    public boolean willItFly(List<Integer> q, int w) {
        if (q.size() == 1) {
            return true;
        }
        int sum = 0;
        int start = 0;
        int end = q.size() - 1;
        while (start < end) {
            if (q.get(start) == q.get(end)) {
                sum += q.get(start);
                start++;
                end--;
            } else {
                return false;
            }
        }
        if (sum > w) {
            return false;
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        // write your code here
        Solution s = new Solution();
        List<Integer> l = new ArrayList<>();
        l.add(1);
        l.add(2);
        l.add(3);
        l.add(4);
        l