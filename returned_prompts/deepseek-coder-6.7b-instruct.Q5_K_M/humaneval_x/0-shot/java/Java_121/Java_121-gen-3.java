        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (i % 2 == 0 && lst.get(i) % 2 != 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}

This solution works by iterating over the list of integers and checking if the current index is even (i.e., if the index is 0, 2, 4, etc.) and if the integer at that index is odd (i.e., if the integer is 1, 3, 5, etc.). If both conditions are met, the integer is added to the sum. Finally, the sum is returned.

In the given examples:
- In the first example, the integers at even positions are 5 (at index 0) and 7 (at index 2), and the sum is 12.
- In the second example, all integers are odd and are at even positions, so the sum is 9.
- In the third example, there are no odd integers at even positions, so the sum is 0.
*/


import java.util.*;
import java.lang.*;

class Solution {
    public int solution(List<Integer> lst) {
        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (i % 2 == 0 && lst.get(i) % 2 != 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(Arrays.asList(5, 8, 7, 1))); // 12
        System.out.println(sol.solution(Arrays.asList(3, 3, 3, 3, 3))); // 9
        System.out.println(sol.solution(Arrays.asList(30, 13, 