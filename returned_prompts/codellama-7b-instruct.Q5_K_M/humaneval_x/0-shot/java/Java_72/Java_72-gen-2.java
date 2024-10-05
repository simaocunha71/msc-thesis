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
        return isBalanced(q) && sum(q) <= w;
    }

    private boolean isBalanced(List<Integer> q) {
        return isBalanced(q, 0);
    }

    private boolean isBalanced(List<Integer> q, int i) {
        if (q.size() == i + 1) return true;
        return q.get(i) == q.get(q.size() - i - 1) && isBalanced(q, i + 1);
    }

    private int sum(List<Integer> q) {
        return sum(q, 0);
    }

    private int sum(List<Integer> q, int i) {
        if (q.size() == i + 1) return q.get(i);
        return q.get(i) + sum(q, i + 1);
