import java.util.*;
import java.lang.*;

class Solution {
    /**
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative(Arrays.asList(3, 1, 2, 4, 5))
    [1, 4, 12, 20]
    >>> derivative(Arrays.asList(1, 2, 3]))
    [2, 6]
     */
    public List<Integer> derivative(List<Integer> xs) {
        if (xs == null || xs.size() < 2) return Collections.emptyList();
        int power = 0;
        for (int n : xs) {
            //power++;
            System.out.println("n:" + n);
        }
        return Arrays.asList(xs).stream().map((n) -> Integer.valueOf(Math.pow(10, power - 1)) * Math.pow(n, power)).collect(Collectors.toList());
    }
}