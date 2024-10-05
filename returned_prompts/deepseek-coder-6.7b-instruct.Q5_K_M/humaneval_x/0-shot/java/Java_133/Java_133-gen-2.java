        int sum = 0;
        for (Double num : lst) {
            sum += Math.ceil(num) * Math.ceil(num);
        }
        return sum;
    }
}

*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        List<Double> lst1 = Arrays.asList(1.0, 2.0, 3.0);
        List<Double> lst2 = Arrays.asList(1.0, 4.0, 9.0);
        List<Double> lst3 = Arrays.asList(1.0, 3.0, 5.0, 7.0);
        List<Double> lst4 = Arrays.asList(1.4, 4.2, 0.0);
        List<Double> lst5 = Arrays.asList(-2.4, 1.0, 1.0);

        System.out.println(solution.sumSquares(lst1)); // 14
        System.out.println(solution.sumSquares(lst2)); // 98
        System.out.println(solution.sumSquares(lst3)); // 84
        System.out.println(solution.sumSquares(lst4)); // 29
        System.out.println(solution.sumSquares(lst5)); // 6
    }
}

/*
Answer:
In the given code, we're iterating through the list of doubles. For each double, we're rounding it up to the nearest integer using the `Math.ceil()` function, then squaring it using the '*' operator, and finally adding this squared value to a running total.

At the end, we're returning the total sum.
*/

// 14
// 98
// 84
// 29
// 6

// The code seems to be correct and should pass the provided test cases.
// Please make sure to test it with other inputs to confirm its correctness.

/*
If