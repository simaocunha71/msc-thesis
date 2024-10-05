import java.util.*;
import java.lang.*;

class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int value = 1;
        int x = 0;
        int y = 0;
        while (value <= n * n) {
            for (int i = 0; i < n; i++) {
                matrix[x][y] = value;
                value++;
                y++;
                if (y == n) {
                    y = 0;
                    x++;
                }
            }
            for (int i = 1; i <= n; i++) {
                if (x == n - 1) {
                    break;
                }
                matrix[x][y] = value;
                value++;
                x++;
            }
            for (int i = 1; i <= n; i++) {
                if (y == 0) {
                    break;
                }
                matrix[x][y] = value;
                value++;
                y--;
            }
            for (int i = 1; i <= n; i++) {
                if (x == 0) {
                    break;
                }
                matrix[x][y] = value;
                value++;
                x--;
            }
        }
        return matrix;
    }
}
