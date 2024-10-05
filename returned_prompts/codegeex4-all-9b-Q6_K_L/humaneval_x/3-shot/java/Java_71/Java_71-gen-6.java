
I will use the first question to show you the structure of the code that you should follow. The other questions will have to be done following the same structure.
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

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < threshold) return true;
            }
        }
        return false;
    }
}

The structure of the code is as follows:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Description of the function
    >>> function_name(parameters)
    Expected result
    >>> function_name(parameters)
    Expected result
     */
    public return_type function_name(parameters) {

        code
        return result;
    }
}