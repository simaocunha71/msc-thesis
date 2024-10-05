import java.util.*;
import java.lang.*;

class Solution {
    public int fruitDistribution(String s, int n) {
        int apples = 0;
        int oranges = 0;
        int mango = 0;
        int[] arr = new int[n];
        String[] str = s.split(" ");
        for (int i = 0; i < str.length; i++) {
            if (str[i].equals("apples")) {
                apples = Integer.parseInt(str[i + 1]);
                i++;
            } else if (str[i].equals("oranges")) {
                oranges = Integer.parseInt(str[i + 1]);
                i++;
            } else if (str[i].equals("mango")) {
                mango = Integer.parseInt(str[i + 1]);
                i++;
            }
        }
        return mango;
    }
}