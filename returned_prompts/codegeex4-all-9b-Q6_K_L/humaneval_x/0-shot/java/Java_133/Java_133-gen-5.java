import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
     */
    public int sumSquares(List<Double> lst) {
        // Create a new list to store the ceiling of each element
        List<Integer> ceilList = new ArrayList<>();

        // Iterate through the input list and add the ceiling of each element to the new list
        for (Double num : lst) {
            ceilList.add((int)Math.ceil(num));
        }

        // Initialize a variable to store the sum of squared numbers
        int sum = 0;

        // Iterate through the new list and add the square of each element to the sum
        for (Integer num : ceilList) {
            sum += num * num;
        }

        // Return the sum of squared numbers
        return sum;
    }
}