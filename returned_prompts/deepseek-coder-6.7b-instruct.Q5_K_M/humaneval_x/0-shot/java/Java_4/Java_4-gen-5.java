        double sum = 0; 
        double mean = 0;
        double mad = 0;

        for (Double number : numbers) {
            sum += number;
        }

        mean = sum / numbers.size();

        for (Double number : numbers) {
            mad += Math.abs(number - mean);
        }

        return mad / numbers.size();
    }
}

*/

import java.util.*;
import java.lang.*;

class Solution {
    public double meanAbsoluteDeviation(List<Double> numbers) {
        double sum = 0; 
        double mean = 0;
        double mad = 0;

        for (Double number : numbers) {
            sum += number;
        }

        mean = sum / numbers.size();

        for (Double number : numbers) {
            mad += Math.abs(number - mean);
        }

        return mad / numbers.size();
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Double> numbers = Arrays.asList(1.0, 2.0, 3.0, 4.0);
        System.out.println(solution.meanAbsoluteDeviation(numbers));
    }
}

This program will compute and print the Mean Absolute Deviation (MAD) of the input list of numbers.

It should return 1.0.
*/

import java.util.*;
import java.lang.*;

class Solution {
    public double meanAbsoluteDeviation(List<Double> numbers) {
        double sum = 0; 
        double mean = 0;
        double mad = 0;

        for (Double number : numbers) {
            sum += number;
        }

        mean = sum / numbers.size();

        for (Double number : numbers) {
            mad += Math.abs(number - mean);
        }

        return mad / numbers.size();
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<