        List<Integer> result = new ArrayList<>();
        String numStr = Integer.toString(Math.abs(num));
        int evenCount = 0;
        int oddCount = 0;

        for (int i = 0; i < numStr.length(); i++) {
            if (Integer.parseInt(String.valueOf(numStr.charAt(i))) % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }

        result.add(evenCount);
        result.add(oddCount);

        return result;
    }
}

// Testing the function
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.evenOddCount(-12));  // Expected: [1, 1]
        System.out.println(sol.evenOddCount(123));  // Expected: [1, 2]
    }
}

*/

//src/main/java/com/virtuslab/internship/exercises/day2/Exercise2.java
package com.virtuslab.internship.exercises.day2;

import java.util.*;

public class Exercise2 {

    public static List<Integer> evenOddCount(int num) {
        List<Integer> result = new ArrayList<>();
        String numStr = Integer.toString(Math.abs(num));
        int evenCount = 0;
        int oddCount = 0;

        for (int i = 0; i < numStr.length(); i++) {
            if (Integer.parseInt(String.valueOf(numStr.charAt(i))) % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }

        result.add(evenCount);
        result.add(oddCount);

        return result;
    }

    public static void main(String[] args) {
        System.out.println(evenOddCount(-12));  // Expected: [1,