
I am not sure what the context is, but here are some comments on your code:

Your code is not formatted properly. You should not mix tabs and spaces. Most editors (e.g., VS Code) allow you to set your editor to use spaces instead of tabs. The spacing between lines should be consistent. 
For the first question, you should use a for-each loop instead of a traditional for loop. This is more readable and you don't need to keep track of indices. 
For the second question, you are using a StringBuilder to build your string. This is good, but you don't need to create a new StringBuilder in each iteration. You can create it once and reuse it. 
For the third question, you can use the Math.floor method to truncate the number. This is more efficient than using the modulo operator. 
For the fourth question, you are using the length method of the String class to get the length of the string. This is good, but you don't need to create a new String in each iteration. You can create it once and reuse it. 

Here is your updated code:

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
        for (double num : numbers) {
            for (double otherNum : numbers) {
                double distance = Math.abs(num - otherNum);
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
    ["()", "(())", "(()