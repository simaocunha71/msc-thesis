
I'll go through each of your questions with some general comments and suggestions.
Q1:
The question is asking you to check if there are any two numbers in the given list that are closer to each other than the given threshold. This is a simple problem that can be solved by iterating over the list and comparing each pair of numbers.
Your solution is correct and efficient, but there is a small mistake in the comment. The function should return true if there are two numbers that are closer to each other than the threshold, not false.
A1:
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

Q2:
The question is asking you to separate the groups of parentheses from the given string. This is a simple problem that can be solved by iterating over the string and keeping track of the current depth of parentheses.
Your solution is correct and efficient, but there is a small mistake in the comment. The function should return the list of separate groups of parentheses, not the list of characters.
A2:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced