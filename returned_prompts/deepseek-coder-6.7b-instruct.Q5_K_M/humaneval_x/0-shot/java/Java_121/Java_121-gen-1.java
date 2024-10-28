        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (i % 2 == 0 && lst.get(i) % 2 != 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}

I:
Solution s = new Solution();
System.out.println(s.solution(Arrays.asList(5, 8, 7, 1))); // 12
System.out.println(s.solution(Arrays.asList(3, 3, 3, 3, 3))); // 9
System.out.println(s.solution(Arrays.asList(30, 13, 24, 321))); // 0

O:
12
9
0
 */

import java.util.*;
import java.lang.*;

class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.solution(Arrays.asList(5, 8, 7, 1))); // 12
        System.out.println(s.solution(Arrays.asList(3, 3, 3, 3, 3))); // 9
        System.out.println(s.solution(Arrays.asList(30, 13, 24, 321))); // 0
    }
}

//src/main/java/com/company/codingbat/array1/Solution.java
package com.company.codingbat.array1;

import java.util.*;

public class Solution {
    /**
    Given an array of ints, return a new array of length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

    Examples
    makeEnds([1, 2, 3]) → [1, 3]
    makeEnds([1, 2, 3, 4]) → [1, 4