import java.util.*;
import java.lang.*;

class Solution {
    /**
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largestSmallestIntegers(Arrays.asList(2, 4, 1, 3, 5, 7)) == (Optional.empty(), Optional.of(1))
    largestSmallestIntegers(Arrays.asList()) == (Optional.empty(), Optional.empty())
    largestSmallestIntegers(Arrays.asList(0)) == (Optional.empty(), Optional.empty())
     */
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst){
        if (lst.isEmpty() || lst.get(0) > 0 ){
            return  new ArrayList<>();
        }
        int pos = -1;
        long neg = Long.MIN_VALUE;
         for (int i : lst) {
             if (pos == -1 && i > 0){ // positive integer case
                pos = i;
                 continue;
             } else if(i < neg && pos > -1){ // negative integer case
                 pos = i ;
             }else{ // both cases
              pos = Math.max(pos, Integer.min(Long.MIN_VALUE, i));
             }
         }
        return new ArrayList<>(new Tuple2<>(pos, lst.get(0)));
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println("" + solution.largestSmallestIntegers(Arrays.asList(-4,-3,5,1,-2)) );
        System.out.println("" + solution.largestSmallestIntegers(Arrays.asList())  );
     }
}