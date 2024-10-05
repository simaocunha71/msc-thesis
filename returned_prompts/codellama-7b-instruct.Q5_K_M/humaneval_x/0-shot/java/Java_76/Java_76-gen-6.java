import java.util.*;
import java.lang.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println(isSimplePower(n, k));
    }
    public static boolean isSimplePower(int x, int n) {
        int k = (int) Math.ceil(Math.log(x)/Math.log(n));
        if (n**k == x)
            return true;
        else
            return false;
    }
}