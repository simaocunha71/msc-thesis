        int sum = 0;
        for(int i=0; i<lst.size(); i++){
            if(i%2 == 0 && lst.get(i)%2 != 0){
                sum += lst.get(i);
            }
        }
        return sum;
    }
}

The code will go through each element in the list. If the index is even and the number is odd, it adds the number to the sum.

The time complexity of the solution is O(n) where n is the length of the list.

The space complexity is O(1) since we only use a single variable to store the sum.
*/

import java.util.*;
import java.lang.*;

class SolutionTest {
    public static void main (String[] args) throws java.lang.Exception {
        Solution sol = new Solution();
        System.out.println(sol.solution(Arrays.asList(5, 8, 7, 1))); //==> 12
        System.out.println(sol.solution(Arrays.asList(3, 3, 3, 3, 3))); //==> 9
        System.out.println(sol.solution(Arrays.asList(30, 13, 24, 321))); //==>0
    }
}

/*
Output:
12
9
0
*/

/*
Test Case Explanation:

For the first test case, the elements at even indices are 5, 7 and 1. The sum of odd elements at even indices is 5 + 1 = 6.

For the second test case, all elements are odd and at even indices, so the sum is 3 + 3 + 3 + 3 = 12.

For the third test case, there are no odd elements at even indices, so the sum is 0.
*/

/*
This code works for the provided examples and the problem statement. However, it does not handle cases where the list is empty or contains null values. You may want to add additional checks for these cases depending on your specific requirements.
*/

/*
In the solution, we are going through the list and checking if the index is even