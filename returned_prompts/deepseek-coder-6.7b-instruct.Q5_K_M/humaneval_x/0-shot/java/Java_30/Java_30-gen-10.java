        return l.stream()
                .filter(x -> x > 0)
                .collect(Collectors.toList());
    }
}

*/

import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> getPositive(List<Integer> l) {
        return l.stream()
                .filter(x -> x > 0)
                .collect(Collectors.toList());
    }
}

//src/main/java/com/example/demo/Main.java
package com.example.demo;

import com.example.demo.Solution;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.getPositive(Arrays.asList(-1, 2, -4, 5, 6))); // [2, 5, 6]
        System.out.println(sol.getPositive(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10))); // [5, 3, 2, 3, 9, 123, 1]
    }
}

//src/test/java/com/example/demo/SolutionTest.java
package com.example.demo;

import com.example.demo.Solution;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {
    Solution solution = new Solution();

    @Test
    void getPositive() {
        List<Integer> input = Arrays.asList(-1, 2, -4, 5, 6);
        List<Integer> expected = Arrays.asList(2, 5, 6);

        assertEquals(expected, solution.getPositive(input));