        StringBuilder sb = new StringBuilder();
        for(int i = 0; i <= n; i++) {
            sb.append(i);
            if(i < n) {
                sb.append(" ");
            }
        }
        return sb.toString();
    }
}

T:
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.stringSequence(0)); // "0"
        System.out.println(solution.stringSequence(5)); // "0 1 2 3 4 5"
    }
}
*/

//src/main/java/com/solution/StringSequence.java
package com.solution;

public class StringSequence {

    public static String stringSequence(int n) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i <= n; i++) {
            sb.append(i);
            if(i < n) {
                sb.append(" ");
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println(stringSequence(0)); // "0"
        System.out.println(stringSequence(5)); // "0 1 2 3 4 5"
    }
}

//src/test/java/com/solution/StringSequenceTest.java
package com.solution;

import com.solution.StringSequence;
import org.junit.Test;
import static org.junit.Assert.*;

public class StringSequenceTest {
    @Test
    public void testStringSequence() {
        assertEquals("0", StringSequence.stringSequence(0));
        assertEquals("0 1 2 3 4 5", StringSequence.stringSequence(5));
    }
}package com.solution;

import java.util.Arrays;

public class SmallestMissingPositive {

    public static int smallestMissingPositive(int[] nums) {
        Arrays.sort(nums);
        int missing = 1;
