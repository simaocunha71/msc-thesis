import java.util.*;
import java.lang.*;

class Solution {
    /**
    pairsSumToZero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairsSumToZero(Arrays.asList(1, 3, 5, 0))
    false
    >>> pairsSumToZero(Arrays.asList(1, 3, -2, 1))
    false
    >>> pairsSumToZero(Arrays.asList(1, 2, 3, 7))
    false
    >>> pairsSumToZero(Arrays.asList(2, 4, -5, 3, 5, 7))
    true
    >>> pairsSumToZero(Arrays.asList(1))
    false
     */
    public boolean pairsSumToZero(List<Integer> l) {
        if (l == null || l.size() < 2) return false;
        boolean[] array = new boolean[l.size()];
        for (int i=0 ; i<array.length ;i++)
            array[i] = false;
        
        int sum = 0;
        for(int i: l){
            sum+=i;
            for(int j=i+1, k=j-1; j>=k && k<l.size() && j<=k ; j--, k++)
                if((array[j] || array[k]) && (sum%i) == 0){
                    sum = sum / i;
                    array[j] = true;
                    array[k] = false;
                }
        }
        
        return (array.length==2);
    }
}