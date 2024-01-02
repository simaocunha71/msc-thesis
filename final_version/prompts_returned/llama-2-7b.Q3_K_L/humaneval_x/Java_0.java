import java.util.*;
import java.lang.*;

class Solution {
    /**
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    >>> hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)
    false
    >>> hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)
    true
     */
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        if (numbers == null || numbers.isEmpty()) return false;
        
        ListIterator<Integer> li = new LinkedListIterator<>(new ArrayList<>(numbers).iterator());
        while (li.hasNext()){
            int i = (int) li.next();
            
            //If current element is greater than previous,  then return false.  
            if(i > threshold && !hasCloseElements(numbers, i - 1)){
                return false;
            } else if (i < threshold && hasCloseElements(numbers, i + 1)) {
               return true;
            }
        }
        
        //If current element is greater than previous,  then return false.  
        int prev = -1;
        while (li.hasNext()){
            int i = (int) li.next();
            
            if(i > threshold && !hasCloseElements(numbers, i - 1)){
                return false;
            } else {
                    //If current element is greater than previous,  then return false.  
                prev = i; 
            }
        }
        
        //If current element is greater than previous,  then return false.  
        return true;
    }
}