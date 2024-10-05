        int count = 0;
        for(int num : arr){
            int sum = 0;
            String strNum = Integer.toString(num);
            for(int i = 0; i < strNum.length(); i++){
                if(strNum.charAt(i) == '-'){
                    continue;
                }
                sum += Integer.parseInt(String.valueOf(strNum.charAt(i)));
            }
            if(sum > 0){
                count++;
            }
        }
        return count;
    }
}

*/

import java.util.*;

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.countNums(Arrays.asList(1, 1, 2))); // expected 3
        System.out.println(solution.countNums(Arrays.asList(-1, 11, -11))); // expected 1
        System.out.println(solution.countNums(Arrays.asList())); // expected 0
    }
}

/*
Explanation:
For example,
In the list [1, 1, 2], the sum of digits of 1 and 2 are both greater than 0, so the count is 3.
In the list [-1, 11, -11], the sum of digits of -1 and -11 are both less than or equal to 0. But we count 11 because its sum of digits 1 + 1 = 2 which is greater than 0. So, the count is 1.
In the empty list, there are no elements, so the count is 0.
*/

/*
Time Complexity: O(n*m) where n is the size of the array and m is the number of digits in the maximum number
Space Complexity: O(1) as we are not using any extra space that scales with the size of the input
*/

/*
Constraints:
1 ≤ n ≤ 100
-100 ≤ arr[i] ≤