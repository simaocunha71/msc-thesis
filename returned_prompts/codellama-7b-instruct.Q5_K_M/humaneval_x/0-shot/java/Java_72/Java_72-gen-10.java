import java.util.*;

class Solution {
    public boolean willItFly(List<Integer> q, int w) {
        // Write your solution here
        int sum = 0;
        for (int i = 0; i < q.size(); i++) {
            sum += q.get(i);
        }
        if (sum > w) {
            return false;
        }
        if (isBalanced(q)) {
            return true;
        }
        return false;
    }

    private boolean isBalanced(List<Integer> q) {
        int size = q.size();
        if (size == 1) {
            return true;
        }
        if (size == 0) {
            return false;
        }
        int sum = 0;
        for (int i = 0; i < q.size(); i++) {
            sum += q.get(i);
        }
        if (sum == 0) {
            return true;
        }
        if (sum < 0) {
            return false;
        }
        int mid = size / 2;
        int leftSum = 0;
        int rightSum = 0;
        for (int i = 0; i < mid; i++) {
            leftSum += q.get(i);
        }
        for (int i = mid; i < q.size(); i++) {
            rightSum += q.get(i);
        }
        if (leftSum == rightSum) {
            return true;
        }
        return false;
    }
}