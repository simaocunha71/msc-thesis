        int oddCountLst1 = 0;
        int evenCountLst2 = 0;

        for (int i : lst1) {
            if (i % 2 != 0) {
                oddCountLst1++;
            }
        }

        for (int i : lst2) {
            if (i % 2 == 0) {
                evenCountLst2++;
            }
        }

        return oddCountLst1 <= evenCountLst2 ? "YES" : "NO";
    }
}

Explanation:

We need to check the number of odd numbers in lst1 and even numbers in lst2.
If there are more odd numbers in lst1 than even numbers in lst2, it is possible to make all numbers in lst1 even by exchanging with elements in lst2. Thus, return "YES".
Otherwise, return "NO".


*/

import java.util.*;
import java.lang.*;

class Solution {
    public static String exchange(List<Integer> lst1, List<Integer> lst2) {
        int oddCountLst1 = 0;
        int evenCountLst2 = 0;

        for (int i : lst1) {
            if (i % 2 != 0) {
                oddCountLst1++;
            }
        }

        for (int i : lst2) {
            if (i % 2 == 0) {
                evenCountLst2++;
            }
        }

        return oddCountLst1 <= evenCountLst2 ? "YES" : "NO";
    }

    public static void main(String[] args) {
        System.out.println(exchange(Arrays.asList(1, 2, 3, 4), Arrays.asList(1, 2, 3, 4))); // "YES"
        System.out.println(exchange(Arrays.asList(1, 2, 3, 4), Arrays.asList(1, 5, 3, 4))); // "NO"
    }
}

