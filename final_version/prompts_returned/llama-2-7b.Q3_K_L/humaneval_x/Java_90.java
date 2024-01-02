import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given a list of integers.
    Write a function nextSmallest() that returns the 2nd smallest element of the list.
    Return null if there is no such element.
    <p>
    nextSmallest(Arrays.asList(1, 2, 3, 4, 5)) == Optional[2]
    nextSmallest(Arrays.asList(5, 1, 4, 3, 2)) == Optional[2]
    nextSmallest(Arrays.asList()) == Optional.empty
    nextSmallest(Arrays.asList(1, 1)) == Optional.empty
     */
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst == null || lst.size() < 2) return null;
         int smallest = lst.get(0);
         for(int i=1;i<=lst.size();i++){
             if(lst.get(i-1) > smallest){
                 smallest = lst.get(i-1);
             }
         }
        return new Optional<>(smallest);
    }
    
}