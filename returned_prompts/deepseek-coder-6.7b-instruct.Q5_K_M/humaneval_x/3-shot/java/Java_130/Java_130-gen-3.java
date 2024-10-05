        List<Integer> result = new ArrayList<>();
        if(n < 0) return result;

        result.add(1);
        if(n == 0) return result;

        result.add(3);
        if(n == 1) return result;

        result.add(2);
        if(n == 2) return result;

        for(int i = 3; i <= n; i++) {
            int next;
            if(i % 2 == 0) {
                next = 1 + i / 2;
            } else {
                next = result.get(i - 1) + result.get(i - 2) + result.get(i + 1);
            }
            result.add(next);
        }

        return result;
    }
}


A: Here is the solution for your query.

import java.util.*;
import java.lang.*;

class Solution {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        Solution s = new Solution();
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(s.separateParenGroups("(  )  (( ))  (( )( ))"));
        System.out.println(s.truncateNumber(3.5));
        System.out.println(s.tri(3));
    }

    /**
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    >>> hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)
    false
    >>> hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)
    true
      */
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        for