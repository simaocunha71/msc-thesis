        int sum = 0;

        for(Double num : lst){
            sum += Math.ceil(num) * Math.ceil(num);
        }

        return sum;
    }
}

Explanation:
In this solution, we iterate through the given list of numbers. For each number, we round it to the upper integer using Math.ceil() and then square it by multiplying it with itself. We add the square of each number to the sum. Finally, we return the sum. 

This solution assumes that the input list is not null and contains at least one element. If this is not the case, we need to add appropriate error checking.
*/

import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        List<Double> lst1 = Arrays.asList(1.0, 2.0, 3.0);
        System.out.println(solution.sumSquares(lst1));  // Output: 14

        List<Double> lst2 = Arrays.asList(1.0, 4.0, 9.0);
        System.out.println(solution.sumSquares(lst2));  // Output: 98

        List<Double> lst3 = Arrays.asList(1.0, 3.0, 5.0, 7.0);
        System.out.println(solution.sumSquares(lst3));  // Output: 84

        List<Double> lst4 = Arrays.asList(1.4, 4.2, 0.0);
        System.out.println(solution.sumSquares(lst4));  // Output: 29

        List<Double> lst5 = Arrays.asList(-2.4, 1.0, 1.0);
        System.out.println(solution.sumSquares(lst5));  // Output: 6
    }
}

/*
Output:
14
98
84
