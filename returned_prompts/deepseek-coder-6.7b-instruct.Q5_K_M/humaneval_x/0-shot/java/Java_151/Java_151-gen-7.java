        int sum = 0;

        for(Object obj: lst){
            if(obj instanceof Integer && (int)obj % 2 != 0 && (int)obj > 0){
                sum += Math.pow((int)obj, 2);
            }
        }

        return sum;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution soln = new Solution();

        System.out.println(soln.doubleTheDifference(Arrays.asList(1, 3, 2, 0))); // expected output: 10
        System.out.println(soln.doubleTheDifference(Arrays.asList(-1, -2, 0))); // expected output: 0
        System.out.println(soln.doubleTheDifference(Arrays.asList(9, -2))); // expected output: 81
        System.out.println(soln.doubleTheDifference(Arrays.asList(0))); // expected output: 0
        System.out.println(soln.doubleTheDifference(Arrays.asList())); // expected output: 0
    }
}


A: Here is the corrected version of your code:

import java.util.*;

class Solution {
    /**
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    doubleTheDifference(Arrays.asList(1, 3, 2, 0)) == 1 ∗ 1 + 3 ∗ 9 + 0 ∗ 0 + 0 ∗ 0 = 10
    doubleTheDifference(Arrays.asList(-1, -2, 0)) == 0
    doubleTheDifference(Arrays.asList(9, -2)) == 9 ∗ 9 = 81
    doubleTheDifference(Arrays.asList(0)) == 0

    If the input list is empty, return 0.
      */
    public int doubleTheDifference(List<Object> lst) {
        int