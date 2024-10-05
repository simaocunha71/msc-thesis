        int sum = 0;

        for(Double num : lst){
            int roundedNum = (int)Math.ceil(num);
            sum += roundedNum * roundedNum;
        }

        return sum;
    }
}

*/

import java.util.*;
import java.lang.*;

class Solution  {
    public int sumSquares(List<Double> lst) {
        int sum = 0;

        for(Double num : lst){
            int roundedNum = (int)Math.ceil(num);
            sum += roundedNum * roundedNum;
        }

        return sum;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        List<Double> lst1 = Arrays.asList(1.0, 2.0, 3.0);
        List<Double> lst2 = Arrays.asList(1.0, 4.0, 9.0);
        List<Double> lst3 = Arrays.asList(1.0, 3.0, 5.0, 7.0);
        List<Double> lst4 = Arrays.asList(1.4, 4.2, 0.0);
        List<Double> lst5 = Arrays.asList(-2.4, 1.0, 1.0);

        System.out.println(sol.sumSquares(lst1)); //14
        System.out.println(sol.sumSquares(lst2)); //98
        System.out.println(sol.sumSquares(lst3)); //84
        System.out.println(sol.sumSquares(lst4)); //29
        System.out.println(sol.sumSquares(lst5)); //6

    }
}import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a number");
        int num = scan.nextInt();
        boolean