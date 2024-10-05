        if(arr.isEmpty()){
            return Optional.empty();
        }
        int sum = 0;
        int prod = 1;
        for(int num : arr){
            if(num < 0){
                prod *= -1;
            }
            else if(num > 0){
                prod *= 1;
            }
            sum += Math.abs(num);
        }
        return Optional.of(sum * prod);
    }
}

I:
import java.util.*;

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.prodSigns(Arrays.asList(1, 2, 2, -4)));  // -9
        System.out.println(solution.prodSigns(Arrays.asList(0, 1)));  // 0
        System.out.println(solution.prodSigns(Arrays.asList()));  // Optional.empty
    }
}

O:
-9
0
Optional.empty
*/

import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        if(arr.isEmpty()){
            return Optional.empty();
        }
        int sum = 0;
        int prod = 1;
        for(int num : arr){
            if(num < 0){
                prod *= -1;
            }
            else if(num > 0){
                prod *= 1;
            }
            sum += Math.abs(num);
        }
        return Optional.of(sum * prod);
    }
}

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.prodSigns(Arrays.asList(1, 2, 2, -4)));  // -9
        System.out.println(solution.prodSigns(Arrays.asList(0, 1)));  // 0
       