        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));

        if (start > end) {
            return "NO";
        }

        int length = end - start;

        return isPrime(length) ? "YES" : "NO";
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

*/

/*
import java.util.*;

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> interval1 = Arrays.asList(1, 2);
        List<Integer> interval2 = Arrays.asList(2, 3);
        System.out.println(solution.intersection(interval1, interval2));

        interval1 = Arrays.asList(-1, 1);
        interval2 = Arrays.asList(0, 4);
        System.out.println(solution.intersection(interval1, interval2));

        interval1 = Arrays.asList(-3, -1);
        interval2 = Arrays.asList(-5, 5);
        System.out.println(solution.intersection(interval1, interval2));
    }
}
*/

//src/test/java/SolutionTest.java
import org.junit.jupiter.api.Test;
import solution.Solution;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class SolutionTest {
    Solution solution = new Solution();

    @Test
    void testIntersection() {
        List<Integer> interval1 = Arrays.asList(1, 2);
       