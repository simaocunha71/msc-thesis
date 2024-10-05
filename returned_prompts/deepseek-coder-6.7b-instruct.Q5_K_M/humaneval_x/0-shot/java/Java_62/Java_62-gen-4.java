        List<Integer> result = new ArrayList<Integer>();
        for (int i = 1; i < xs.size(); i++) {
            result.add(xs.get(i) * i);
        }
        return result;
    }
}

*/

//src/main/java/com/codewars/kyu8/EvenOrOdd.java
package com.codewars.kyu8;

public class EvenOrOdd {
    /**
     * Given a number, return a string indicating if it is even or odd.
     *
     * @param num the number to check
     * @return a string indicating whether the number is even or odd
     */
    public static String even_or_odd(int num) {
        return num % 2 == 0 ? "Even" : "Odd";
    }
}

//src/main/java/com/codewars/kyu8/NoBoringZeros.java
package com.codewars.kyu8;

public class NoBoringZeros {
    /**
     * Given a number, return the number of trailing zeros in its factorial.
     *
     * @param n the number to find the trailing zeros in its factorial
     * @return the number of trailing zeros in n's factorial
     */
    public static int noBoringZeros(int n) {
        int count = 0;
        for (int i = 5; n / i >= 1; i *= 5) {
            count += n / i;
        }
        return count;
    }
}

//src/main/java/com/codewars/kyu8/SquareSum.java
package com.codewars.kyu8;

public class SquareSum {
    /**
     * Given an array of numbers, return the sum of the squares of each number.
     *
     * @param numbers the array of numbers
     * @return the sum of the squares of each number
     */
    public static int squareSum(int[] numbers) {
        int sum = 0;
        for (int number : numbers) {
            sum += number * number;
       