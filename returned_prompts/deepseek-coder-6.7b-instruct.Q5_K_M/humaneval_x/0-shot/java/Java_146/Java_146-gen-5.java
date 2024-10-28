        int count = 0;
        Set<Integer> oddDigits = new HashSet<>(Arrays.asList(1, 3, 5, 7, 9));

        for (int num : nums) {
            if (Math.abs(num) > 10 && oddDigits.contains(num % 10) && oddDigits.contains(num / 1000000000)) {
                count++;
            }
        }

        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.specialFilter(Arrays.asList(15, -73, 14, -15))); // 1
        System.out.println(solution.specialFilter(Arrays.asList(33, -2, -3, 45, 21, 109))); // 2
    }
}

This solution first creates a HashSet of the odd digits. Then it iterates over the list of numbers. For each number, it checks if the absolute value is greater than 10 and if the last digit and the first digit of the number are in the HashSet. If both conditions are true, it increases the count.
The time complexity of this solution is O(n), where n is the size of the input list.
The space complexity of this solution is O(1), because the space used does not increase with the size of the input list.
*/

import java.util.*;
import java.lang.*;

class Solution 
{
    public int specialFilter(List<Integer> nums) 
    {
        int count = 0;
        Set<Integer> oddDigits = new HashSet<>(Arrays.asList(1, 3, 5, 7, 9));

        for (int num : nums) 
        {
            if (Math.abs(num) > 10 && oddDigits.contains(Math.abs(num) / 10 % 10) && oddDigits.contains(num / 1000000000))