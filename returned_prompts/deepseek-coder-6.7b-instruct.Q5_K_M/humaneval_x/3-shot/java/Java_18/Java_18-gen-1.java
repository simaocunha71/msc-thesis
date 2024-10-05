        int count = 0;
        int index = 0;

        while  (true)  {
            index = string.indexOf(substring, index);
            if  (index  != -1)  {
                count += 1;
                index  += substring.length();
            } else  break;
        }

        return count;
     }
}


A: Here are the corrections.
Q1:
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
        for  (int i = 0; i < numbers.size() - 1; i++) {
            for  (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if  (distance < threshold) return true;
            }
        }
        return false;
    }
}

Q2:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced  (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separateParenGroups("(  )  (( ))  (( )( ))")
    ["()", "(())", "(()())"]
      */
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList