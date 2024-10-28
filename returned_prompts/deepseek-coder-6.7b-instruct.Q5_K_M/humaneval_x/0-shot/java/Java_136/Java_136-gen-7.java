        List<Optional<Integer>> result = new ArrayList<>(Arrays.asList(Optional.empty(), Optional.empty()));
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        boolean flag1 = false, flag2 = false;

        for(int i : lst){
            if(i < 0 && i > max){
                max = i;
                flag1 = true;
            }
            if(i > 0 && i < min){
                min = i;
                flag2 = true;
            }
        }
        if(flag1) result.set(0, Optional.of(max));
        if(flag2) result.set(1, Optional.of(min));

        return result;
    }
}

Explanation:
This solution is pretty straightforward. The function iterates through the list and checks if the current integer is a negative one and if it's larger than the current max value. If so, it updates the max value and sets the flag to true. The same logic applies for positive integers.
Finally, it returns a list of Optionals, where the first Optional contains the largest negative integer if it was found, and the second Optional contains the smallest positive integer if it was found. If neither was found, the respective Optional is empty.
This solution has a time complexity of O(n), where n is the size of the list.

*/

import java.util.*;
import java.lang.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst) {
        List<Optional<Integer>> result = new ArrayList<>(Arrays.asList(Optional.empty(), Optional.empty()));
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        boolean flag1 = false, flag2 = false;

        for (int i : lst) {
            if (i < 0 && i > max) {
                max = i;
                flag1 = true;
            }
            if (i > 0 && i < min) {
                min = i;
                flag2 = true;
            }
        }
        if (flag1) result.set(0, Optional