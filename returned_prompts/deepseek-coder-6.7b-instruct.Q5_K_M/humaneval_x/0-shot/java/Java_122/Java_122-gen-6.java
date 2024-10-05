        int sum = 0;
        for (int i = 0; i < k; i++) {
            if (arr.get(i) < 10 || arr.get(i) >= 100) {
                sum += arr.get(i);
            }
        }
        return sum;
    }
}

*/

//Main.java
import java.util.*;
import java.lang.*;

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution sol = new Solution();
        List<Integer> arr = new ArrayList<Integer>(Arrays.asList(111,21,3,4000,5,6,7,8,9));
        int k = 4;
        int result = sol.addElements(arr, k);
        System.out.println(result);
    }
}

//SolutionTest.java
import java.util.*;
import org.junit.*;
import static org.junit.Assert.*;

public class SolutionTest {
    @Test
    public void testAddElements() {
        Solution sol = new Solution();
        List<Integer> arr1 = new ArrayList<Integer>(Arrays.asList(111,21,3,4000,5,6,7,8,9));
        List<Integer> arr2 = new ArrayList<Integer>(Arrays.asList(100,200,300,400,500,600,700,800,900));
        List<Integer> arr3 = new ArrayList<Integer>(Arrays.asList(999,100,200,300,400,500,600,700,800));
        assertEquals(24, sol.addElements(arr1, 4));
        assertEquals(1500, sol.addElements(arr2, 6));
        assertEquals(2990, sol.addElements(arr3, 8));
    }
}

//Solution.java
import java.util.*;
import java.lang.*;
