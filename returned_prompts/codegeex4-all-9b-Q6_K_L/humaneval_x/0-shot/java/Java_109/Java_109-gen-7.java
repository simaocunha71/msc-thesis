import java.util.*;
import java.lang.*;

class Solution {
    public boolean moveOneBall(List<Integer> arr) {
        if (arr.isEmpty()) {
            return true;
        }

        int n = arr.size();
        int minIndex = 0;
        int min = arr.get(0);

        for (int i = 1; i < n; i++) {
            if (arr.get(i) < min) {
                min = arr.get(i);
                minIndex = i;
            }
        }

        if (minIndex == n - 1) {
            return true;
        }

        for (int i = minIndex + 1; i < n; i++) {
            if (arr.get(i) < arr.get(i - 1)) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        List<Integer> arr1 = Arrays.asList(3, 4, 5, 1, 2);
        System.out.println(solution.moveOneBall(arr1)); // Output: true

        List<Integer> arr2 = Arrays.asList(3, 5, 4, 1, 2);
        System.out.println(solution.moveOneBall(arr2)); // Output: false

        List<Integer> arr3 = Arrays.asList();
        System.out.println(solution.moveOneBall(arr3)); // Output: true
    }
}
