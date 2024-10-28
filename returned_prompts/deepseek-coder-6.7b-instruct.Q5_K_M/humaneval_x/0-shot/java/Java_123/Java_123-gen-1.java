        List<Integer> oddCollatz = new ArrayList<>();
        while (n != 1) {
            if (n % 2 != 0) {
                oddCollatz.add(n);
            }
            n = (n % 2 == 0) ? n/2 : 3*n + 1;
        }
        oddCollatz.add(1);
        Collections.sort(oddCollatz);
        return oddCollatz;
    }
}


The solution is a simple iteration over the Collatz sequence starting from n until we reach 1. If the current number is odd, we add it to the list. After the loop, we add 1 to the list as it is always the last number in the sequence and sort the list before returning it.

The time complexity of this solution is O(n) because we iterate over the Collatz sequence of length n. The space complexity is also O(n) because in the worst case (when n is 1), we store all numbers in the sequence in the list.
*/

//main.java
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.getOddCollatz(5));  // prints [1, 5]
    }
}

//test/SolutionTest.java
import org.junit.Test;
import java.util.Arrays;
import static org.junit.Assert.*;

public class SolutionTest {
    @Test
    public void testGetOddCollatz() {
        Solution solution = new Solution();
        assertEquals(Arrays.asList(1, 5), solution.getOddCollatz(5));
        assertEquals(Arrays.asList(1, 5, 11, 23, 47), solution.getOddCollatz(10));
        assertEquals(Arrays.asList(1), solution.getOddCollatz(1));
    }
}

//test/SolutionTest2.java
import org.junit.Test;
import java.util.Arrays;
import static org.junit.Assert.*;

