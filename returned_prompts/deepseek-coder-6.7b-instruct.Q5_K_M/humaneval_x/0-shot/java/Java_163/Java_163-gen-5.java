        List<Integer> list = new ArrayList<>();

        // Swap if a > b
        if(a > b) {
            int temp = a;
            a = b;
            b = temp;
        }

        for(int i = a; i <= b; i++) {
            if(i % 2 == 0) {
                list.add(i);
            }
        }

        return list;
    }
}

This is the solution to the problem. It first checks if a is greater than b. If so, it swaps the two values. Then, it iterates from a to b (inclusive) and checks if the current number is divisible by 2 (i.e., it's even). If so, it adds the number to the list. Finally, it returns the list of even integers between a and b.
*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.generateIntegers(2, 8));
        System.out.println(solution.generateIntegers(8, 2));
        System.out.println(solution.generateIntegers(10, 14));
    }
}

//tests/TestSolution.java
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

class TestSolution {

    Solution solution = new Solution();

    @Test
    void testGenerateIntegers() {
        List<Integer> expected1 = Arrays.asList(2, 4, 6, 8);
        List<Integer> expected2 = Arrays.asList(2, 4, 6, 8);
        List<Integer> expected3 = Arrays.asList();
        assertEquals(expected1, solution.generateIntegers(2, 8));
        assertEquals(expected2, solution.generateIntegers(8, 2));
        assertEquals(expected3, solution.generateIntegers(10, 14));
    }
}

