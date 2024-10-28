
Your first solution is correct.
Your second solution is correct, however, the algorithm can be improved:
Instead of checking every character, you can iterate over the string twice. First, you count the number of parentheses and store it in an array. Then, you iterate over the array and for each parenthesis, you increase the current depth until you encounter the matching closing parenthesis. Then you reset the current depth and continue to the next parenthesis.
Your third solution is correct, however, the algorithm can be improved:
Instead of using the modulo operator, you can use the decimal part of the number to get the decimal part. For example, if the number is 3.5, the decimal part is 0.5. If the number is 3.0, the decimal part is 0.0. You can use the Math.floor() function to get the integer part of the number and subtract it from the original number to get the decimal part.
Your fourth solution is correct, however, the algorithm can be improved:
Instead of iterating over the string twice, you can iterate over the string once. For each character, you increase the current depth if it is an opening parenthesis and decrease the current depth if it is a closing parenthesis. Then, you store the current depth in the array and continue to the next character.
Here is the improved version of your code:
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
            for