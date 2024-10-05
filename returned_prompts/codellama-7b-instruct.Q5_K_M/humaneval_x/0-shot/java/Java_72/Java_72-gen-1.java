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
        // Write your code here
        boolean balanced = isBalanced(q);
        int sum = calculateSum(q);
        return balanced && sum <= w;
    }
    private int calculateSum(List<Integer> q) {
        int sum = 0;
        for (int i = 0; i < q.size(); i++) {
            sum += q.get(i);
        }
        return sum;
    }
    private boolean isBalanced(List<Integer> q) {
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < q.size(); i++) {
            stack.push(q.get(i));
        }
        while (stack.size() > 1) {
            int first = stack.pop();
            int second = stack.pop();
            if (first != second) {
                return false;
            }
        }
        return