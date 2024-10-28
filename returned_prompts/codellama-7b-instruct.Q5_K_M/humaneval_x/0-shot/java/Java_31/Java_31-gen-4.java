
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        for (int i = 0; i < N; i++) {
            if (A[i] == 0) {
                System.out.println("0");
            } else if (isPrime(A[i])) {
                System.out.println("1");
            } else {
                System.out.println("-1");
            }
        }
    }

    public static boolean isPrime(int n) {
        if (n == 2 || n == 3 || n == 5 || n == 7) {
            return true;
        }

        for (int i = 2; i < Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

