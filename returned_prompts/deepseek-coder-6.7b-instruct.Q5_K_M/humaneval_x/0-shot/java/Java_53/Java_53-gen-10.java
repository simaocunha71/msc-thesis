        return x + y;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.add(2, 3)); // 5
        System.out.println(solution.add(5, 7)); // 12
    }
}

*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.add(2, 3)); // 5
        System.out.println(solution.add(5, 7)); // 12
    }
}

class Solution {
    public int add(int x, int y) {
        return x + y;
    }
}

//src/main/java/com/javapractices/Main2.java
package com.javapractices;

import com.javapractices.solutions.Solution;

public class Main2 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.add(2, 3)); // 5
        System.out.println(solution.add(5, 7)); // 12
    }
}

//src/test/java/com/javapractices/solutions/SolutionTest.java
package com.javapractices.solutions;

import com.javapractices.solutions.Solution;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class SolutionTest {
    @Test
    public void testAdd() {
        Solution solution = new Solution();
        assertEquals(5, solution.add(2, 3));
        assertEquals(12, solution.add(5, 7));
    }
}package com.javapractices;

public class Main1 {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}

// This is a simple program that prints "Hello, Java!" to