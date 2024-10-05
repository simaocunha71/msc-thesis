        List<Integer> result = new ArrayList<>();
        int minEvenVal = Integer.MAX_VALUE;
        int minEvenIndex = -1;

        for (int i = 0; i < arr.size(); i++) {
            int val = arr.get(i);
            if (val < minEvenVal && val % 2 == 0) {
                minEvenVal = val;
                minEvenIndex = i;
            }
        }

        if (minEvenIndex != -1) {
            result.add(minEvenVal);
            result.add(minEvenIndex);
        }

        return result;
    }
}

The solution works by iterating through the input list, checking each value to see if it's even and smaller than the current smallest even value found. If it is, we update the smallest even value and its index.
After the loop, we return the smallest even value and its index if we found any, otherwise we return an empty list.
This solution has a time complexity of O(n), where n is the number of elements in the input list, and a space complexity of O(1), as we only use a constant amount of extra space.

*/

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1
        List<Integer> arr1 = Arrays.asList(4, 2, 3);
        System.out.println(solution.pluck(arr1));  // Output: [2, 1]

        // Test case 2
        List<Integer> arr2 = Arrays.asList(1, 2, 3);
        System.out.println(solution.pluck(arr2));  // Output: [2, 1]

        // Test case 3
        List<Integer> arr3 = Arrays.asList();
        System.out.println(solution.pluck(arr3));  // Output: []

        // Test case 4
        List<Integer> arr4 = Arrays.asList(5, 0, 3, 0, 4, 2);
        System