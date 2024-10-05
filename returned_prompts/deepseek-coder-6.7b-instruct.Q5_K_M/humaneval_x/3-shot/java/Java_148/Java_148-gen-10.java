        List<String> planets_order = Arrays.asList("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune");
        int index1 = planets_order.indexOf(planet1);
        int index2 = planets_order.indexOf(planet2);

        if  (index1  != -1  && index2  != -1 ) {
            return planets_order.subList(Math.min(index1, index2) + 1, Math.max(index1, index2));
        } else {
            return new ArrayList<>();
        }
     }
}


A: import java.util.*;
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
        for(int i = 0; i < numbers.size()-1; i++) {
            for(int j = i+1; j < numbers.size(); j++) {
                if(Math.abs(numbers.get(i) - numbers.get(j)) < threshold) {
                    return true;
                }
            }
        }
        return false;
    }
}

