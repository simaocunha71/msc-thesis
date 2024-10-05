        List<Integer> copy = new ArrayList<Integer>(array);
        Collections.sort(copy);
        int sum = array.get(0) + array.get(array.size() - 1);
        if (sum % 2 == 0) {
            Collections.reverse(copy);
        }
        return copy;
    }
}

*/

import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        List<Integer> copy = new ArrayList<Integer>(array);
        Collections.sort(copy);
        int sum = array.get(0) + array.get(array.size() - 1);
        if (sum % 2 == 0) {
            Collections.reverse(copy);
        }
        return copy;
    }
}

//src/com/company/Main.java
package com.company;

import com.company.Solution;

import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> array = Arrays.asList(2, 4, 3, 0, 1, 5, 6);
        System.out.println(solution.sortArray(array));
    }
}/*
