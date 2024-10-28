
Your code is mostly correct. Here are a few things I noticed:

In the first question, you do not need the outer loop. You can iterate over the list just once and compare each number with the rest of the list. This will also improve the time complexity from O(n^2) to O(n).
In the second question, you do not need to use StringBuilder and current_depth. You can directly add the parentheses to the result list when you encounter an opening parenthesis and remove it when you encounter a closing parenthesis. This will also simplify the code.
In the third question, you do not need to use Math.abs. The modulo operator already returns a non-negative value. You can just use number % 1.0.
In the fourth question, you do not need to use stream().distinct(). You can directly use Set to remove duplicates. This will also improve the time complexity from O(n^2) to O(n).

Here is the updated code:

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

import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separateParenGroups("( ) (( )) (( )( ))")
    ["()", "(())", "(()())"]
     */
    public List