import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.

    Examples
    solution(Arrays.asList(5, 8, 7, 1)) ==> 12
    solution(Arrays.asList(3, 3, 3, 3, 3)) ==> 9
    solution(Arrays.asList(30, 13, 24, 321)) ==>0
     */
    public int solution(List<Integer> lst) {
        if (lst == null || lst.size() <= 0){
            return -1;
        } else{
            List<Integer> odd = new ArrayList<>();
            //Odd
            for(int i=0;i<lst.size();i++){
                if(lst.get(i)%2 == 1 && i % 2 == 0){
                    odd.add(lst.get(i));
                }
            }
            //Even
            for(int i=0;i<lst.size();i++){
                if (lst.get(i)%2 == 1 && i % 2 != 0){
                    return lst.stream().filter((a)->lst.get(a).equals(lst.get(i))).count() * odd.stream().mapToInt(Integer::intValue).sum();
                } else {
                    continue;
                }
            }
        }
        return 0;
    }
}