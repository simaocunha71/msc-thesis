        int count = 0;
        int i = 0;
        int j = arr.size() - 1;
        while (i <= j) {
            if (arr.get(i) != arr.get(j)) {
                count++;
            }
            i++;
            j--;
        }
        return count;
    }
}

This solution works by using two pointers, one at the beginning and one at the end of the array. It then compares the elements at these positions, and if they are not equal, increments a count. It then moves the pointers towards the center of the array, and repeats this process until it has checked all pairs of elements.

The time complexity of this solution is O(n), where n is the size of the array, because it only needs to iterate over the array once. The space complexity is O(1), because it only uses a constant amount of extra space to store the count and the indices i and j.

I hope this helps, and I'm sorry if there are any mistakes in the code.

*/

import java.util.*;
import java.lang.*;

class Solution {
    public int smallestChange(List<Integer> arr) {
        int count = 0;
        int i = 0;
        int j = arr.size() - 1;
        while (i <= j) {
            if (arr.get(i) != arr.get(j)) {
                count++;
            }
            i++;
            j--;
        }
        return count;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.smallestChange(Arrays.asList(1,2,3,5,4,7,9,6))); // should print 4
        System.out.println(solution.smallestChange(Arrays.asList(1, 2, 3, 4, 3, 2, 2))); // should print 1
        System.out.println(solution.smallestChange(Arrays.asList(1, 2, 3, 2, 1))); //