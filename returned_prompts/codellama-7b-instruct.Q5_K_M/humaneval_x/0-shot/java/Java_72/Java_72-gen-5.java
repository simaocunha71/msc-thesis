import java.util.*;

class Solution {
    public int[][] solve(int[][] mat) {
        // write your code here
        int n = mat.length;
        int m = mat[0].length;
        int[][] result = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                result[i][j] = mat[i][j] + mat[i][j+1] + mat[i+1][j] + mat[i+1][j+1];
            }
        }
        return result;
    }
}



