        int sum = 0;
        while(N > 0) {
            sum += N % 10;
            N /= 10;
        }
        return Integer.toBinaryString(sum);
    }
}

*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solve(1000)); // should print 1
        System.out.println(solution.solve(150)); // should print 110
        System.out.println(solution.solve(147)); // should print 1100
    }
}import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
        int[][] matrix = new int[n][m];
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                matrix[i][j] = scan.nextInt();
            }
        }
        int r = scan.nextInt();
        int c = scan.nextInt();
        int[][] kernel = new int[r][c];
        for(int i=0; i<r; i++) {
            for(int j=0; j<c; j++) {
                kernel[i][j] = scan.nextInt();
            }
        }
        int[][] result = convolve(matrix, kernel);
        for(int i=0; i<result.length; i++) {
            for(int j=0; j<result[0].length; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static int[][] convolve(int[][] matrix, int[][] kernel) {
        int n = matrix.length;
        int m = matrix[0].length