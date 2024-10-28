        int sum = 0;
        for(int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.sumToN(30));
        System.out.println(solution.sumToN(100));
        System.out.println(solution.sumToN(5));
        System.out.println(solution.sumToN(10));
        System.out.println(solution.sumToN(1));
    }
}

This program is a simple Java program that calculates the sum of numbers from 1 to n, where n is an integer. The function `sumToN` uses a for loop to iterate from 1 to n and accumulate the sum in the `sum` variable. After the loop, it returns the sum.

The main method tests the `sumToN` function with some inputs. The results are printed to the console.

The time complexity of this program is O(n) because there is a single loop that runs n times. The space complexity is O(1) because only a constant amount of space is used to store the sum and the loop variable.

This program should run without any issues and produce the expected output.
    */

import java.util.*;
import java.lang.*;

class Solution {
    public int sumToN(int n) {
        int sum = 0;
        for(int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.sumToN(30));
        System.out.println(solution.sumToN(100));
        System.out.println(solution.sumToN(5));
        System.out.println(solution.sumToN(10));
        System.out.println(solution.sumTo