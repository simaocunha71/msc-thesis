import java.util.*;
import java.lang.*;

class Solution {
    /**
     * @param A: an integer array
     * @return: the number of unique values in the array
     */
    public int countUnique(int[] A) {
        // write your code here
        Set<Integer> set = new HashSet<>();
        for (int i : A) {
            set.add(i);
        }
        return set.size();
    }
}



B:
import java.util.*;
import java.lang.*;

class Solution {
    /**
     * @param A: an integer array
     * @return: the number of unique values in the array
     */
    public int countUnique(int[] A) {
        // write your code here
        Set<Integer> set = new HashSet<>();
        for (int i : A) {
            set.add(i);
        }
        return set.size();
    }
}



C:
import java.util.*;
import java.lang.*;

class Solution {
    /**
     * @param A: an integer array
     * @return: the number of unique values in the array
     */
    public int countUnique(int[] A) {
        // write your code here
        if (A == null || A.length == 0) {
            return 0;
        }
        Arrays.sort(A);
        int count = 0;
        for (int i = 0; i < A.length; i++) {
            if (i == 0 || A[i] != A[i - 1]) {
                count++;
            }
        }
        return count;
    }
}



D:
import java.util.*;
import java.lang.*;

class Solution {
    /**
     * @param A: an integer array
     * @return: the number of unique values in the array
     */
    public int countUnique(int[] A) {
        // write your code here
        if (A == null || A.length == 0) {
            return 0;
        }
        int count = 0;
