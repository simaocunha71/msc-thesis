        int count = 0;
        int i = 0, j = arr.size() - 1;
        while (i <= j) {
            if (arr.get(i) == arr.get(j)) {
                i++;
                j--;
            } else if (arr.get(i) > arr.get(j)) {
                arr.set(j, arr.get(i));
                count++;
                i++;
                j--;
            } else if (arr.get(i) < arr.get(j)) {
                arr.set(i, arr.get(j));
                count++;
                i++;
                j--;
            }
        }
        return count;
    }
}

The solution checks if the array is a palindrome by comparing elements from the start and end of the array. If they are not equal, it increments the count of changes and replaces the greater value with the smaller one. If the elements are equal, it moves on to the next pair of elements. The time complexity of this solution is O(n), where n is the size of the array.
*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.smallestChange(Arrays.asList(1,2,3,5,4,7,9,6))); // 4
        System.out.println(solution.smallestChange(Arrays.asList(1, 2, 3, 4, 3, 2, 2))); // 1
        System.out.println(solution.smallestChange(Arrays.asList(1, 2, 3, 2, 1))); // 0
    }
}
/*
Output:
4
1
0
*/

//src/main/java/com/codingbat/java/Array3/Solution2.java
package com.codingbat.java.Array3;

import java.util.Arrays;

public class Solution2 {
    public int[] evenOdd(int[] nums) {
        int even = 0;
        int odd =