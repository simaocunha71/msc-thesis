import java.util.*;
import java.lang.*;

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int[] array = A;
        Arrays.sort(array);
        int max = 0;
        int i = 0;
        int j = array.length - 1;
        while (i < j) {
            if (array[i] + array[j] == 0) {
                max = array[i] == 0 ? array[j] : array[i];
                break;
            }
            i++;
            j--;
        }
        return max;
    }
}

