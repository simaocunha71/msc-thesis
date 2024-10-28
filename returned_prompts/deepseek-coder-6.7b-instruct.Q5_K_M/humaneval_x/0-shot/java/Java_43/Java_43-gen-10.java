        HashSet<Integer> set = new HashSet<Integer>();
        for(int num : l){
            if(set.contains(-num)){
                return true;
            }
            set.add(num);
        }
        return false;
    }
}

Explanation:
This solution uses a HashSet to keep track of the numbers in the list. As we iterate through the list, we check if the set already contains the negation of the current number. If it does, it means we've found two numbers that sum to zero, so we return true. If we reach the end of the list without finding such a pair, we return false.

Time Complexity:
The time complexity of this solution is O(n), where n is the length of the list. This is because we perform a single pass over the list.

Space Complexity:
The space complexity of this solution is also O(n), as in the worst case we may need to store all the elements in the list in the HashSet.
 */

import java.util.*;
import java.lang.*;

class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();

        System.out.println(solution.pairsSumToZero(Arrays.asList(2, 4, -5, 3, 5, 7))); // true
        System.out.println(solution.pairsSumToZero(Arrays.asList(1, 3, 5, 0))); // false
        System.out.println(solution.pairsSumToZero(Arrays.asList(1, 3, -2, 1))); // false
        System.out.println(solution.pairsSumToZero(Arrays.asList(1, 2, 3, 7))); // false
        System.out.println(solution.pairsSumToZero(Arrays.asList(1))); // false
    }
}


















































