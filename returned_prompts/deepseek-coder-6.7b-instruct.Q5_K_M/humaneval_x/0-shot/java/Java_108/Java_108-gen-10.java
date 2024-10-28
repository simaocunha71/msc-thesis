        int count = 0;

        for (Integer num : arr) {
            int sum = 0;
            if (num < 0) {
                String str = num.toString();
                for (int i = 1; i < str.length(); i++) {
                    sum += Integer.parseInt(String.valueOf(str.charAt(i)));
                }
                sum = sum * -1;
            } else {
                String str = num.toString();
                for (int i = 0; i < str.length(); i++) {
                    sum += Integer.parseInt(String.valueOf(str.charAt(i)));
                }
            }
            if (sum > 0) {
                count++;
            }
        }
        return count;
    }
}

*/

//SolutionTest.java
import org.junit.Test;
import static org.junit.Assert.*;
import java.util.*;

public class SolutionTest {
    @Test
    public void testCountNums() {
        Solution s = new Solution();
        assertEquals(0, s.countNums(Arrays.asList()));
        assertEquals(1, s.countNums(Arrays.asList(-1, 11, -11)));
        assertEquals(3, s.countNums(Arrays.asList(1, 1, 2)));
    }
}

//Test.java
import org.junit.Test;
import static org.junit.Assert.*;
import java.util.*;

public class SolutionTest {
    @Test
    public void testCountNums() {
        Solution s = new Solution();
        assertEquals(0, s.countNums(Arrays.asList()));
        assertEquals(1, s.countNums(Arrays.asList(-1, 11, -11)));
        assertEquals(3, s.countNums(Arrays.asList(1, 1, 2)));
    }
}

//Test1.java
import org.junit.Test;
import static org.junit.Assert.*;
import java.util.*;

public class SolutionTest {
    @Test
    public void test