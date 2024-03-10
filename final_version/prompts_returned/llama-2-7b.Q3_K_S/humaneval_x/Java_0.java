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
        
        Map <Integer, Double > map = new HashMap<>();
        for(int i=0;i<numbers.size();i++){
            map.putIfAbsent(numbers.get(i), 1.0);
        }
        if(map == null || map.isEmpty()) return false;
        
        ListIterator <Double> it = map.keySet().listIterator();
        while (it.hasNext()) {
            if (!threshold.equals(Math.abs(it.nextLongValue()))) {
                return true;
            }
        }
        return false;
    }
}