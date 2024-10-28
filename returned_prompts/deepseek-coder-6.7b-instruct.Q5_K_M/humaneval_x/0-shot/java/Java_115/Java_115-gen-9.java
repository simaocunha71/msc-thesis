        int total = 0;
        for (List<Integer> row : grid) {
            for (Integer cell : row) {
                total += cell;
            }
        }
        return (total + capacity - 1) / capacity;
    }
}

*/

//src/main/java/com/example/code/maxFill/MaxFillApplication.java
package com.example.code.maxFill;

import com.example.code.maxFill.Solution;

import java.util.Arrays;
import java.util.List;

public class MaxFillApplication {

    public static void main(String[] args) {

        Solution solution = new Solution();

        List<List<Integer>> grid = Arrays.asList(
                Arrays.asList(0,0,1,0),
                Arrays.asList(0,1,0,0),
                Arrays.asList(1,1,1,1)
        );
        int bucketCapacity = 1;

        int result = solution.maxFill(grid, bucketCapacity);

        System.out.println("Result: " + result);
    }
}

//src/test/java/com/example/code/maxFill/SolutionTest.java
package com.example.code.maxFill;

import com.example.code.maxFill.Solution;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void maxFill() {

        Solution solution = new Solution();

        List<List<Integer>> grid1 = Arrays.asList(
                Arrays.asList(0,0,1,0),
                Arrays.asList(0,1,0,0),
                Arrays.asList(1,1,1,1)
        );
        int bucketCapacity1 = 1;
        assertEquals(6, solution.maxFill(grid1, bucketCapacity1));

        List<List<Integer>> grid2 =