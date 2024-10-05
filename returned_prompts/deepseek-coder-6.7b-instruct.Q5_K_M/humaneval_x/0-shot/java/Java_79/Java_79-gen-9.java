        String binary = Integer.toBinaryString(decimal);
        return "db"+binary+"db";
    }
}

*/

//tests/DecimalToBinaryTest.java
import org.junit.Test;
import static org.junit.Assert.*;
import Solution;

public class DecimalToBinaryTest {
    @Test
    public void testDecimalToBinary() {
        Solution sol = new Solution();
        assertEquals("db1111db", sol.decimalToBinary(15));
        assertEquals("db100000db", sol.decimalToBinary(32));
        assertEquals("db11010db", sol.decimalToBinary(26));
        assertEquals("db111111db", sol.decimalToBinary(63));
    }
}