    ArrayList<Integer> result = new ArrayList<Integer>();

    for (int i = 0; i < game.size(); i++) {
        result.add(Math.abs(game.get(i) - guess.get(i)));
    }

    return result;
    }
}

*/

//src/main/java/com/codility/lesson2/OddOccurrencesInArray.java
package com.codility.lesson2;

import java.util.HashSet;
import java.util.Set;

public class OddOccurrencesInArray {

    /**
     * A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.
     *
     * For example, in array A such that:
     *
     *   A[0] = 9  A[1] = 3  A[2] = 9
     *   A[3] = 3  A[4] = 9  A[5] = 7
     *   A[6] = 9
     *
     * the elements of A with values 3 and 7 have been paired together:
     *
     *   A[0] = 9, A[2] = 9, A[4] = 9, A[6] = 9
     *
     * and the element A[1] = 3, A[3] = 3, A[5] = 7 is unpaired.
     *
     * The goal is to find the value of the unpaired element.
     *
     * Write a function:
     *
     * class Solution { public int solution(int[] A); }
     *
     * that, given an array A consisting of N integers, returns the value of the unpaired element.
     *
     * For example, given array A such that:
     *
     *   A[0] = 9  A[1] = 3  A[2] = 9
     *   A[3] = 3  A[4] = 9  A[5] = 7
     *