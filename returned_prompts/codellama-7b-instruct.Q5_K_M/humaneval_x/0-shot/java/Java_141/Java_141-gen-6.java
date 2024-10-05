import java.util.*;
import java.lang.*;

class Solution {
    public int[] solution(int[] A) {
        int[] result = new int[A.length];
        for (int i = 0; i < A.length; i++) {
            result[i] = A[i] * 2;
        }
        return result;
    }
}
