import java.util.*;

class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();
        System.out.println(isEqualToSumEven(n) ? "Yes" : "No");
    }

    static boolean isEqualToSumEven(int n) {
        for (int i = 2; i <= n; i += 2) {
            int sum = i;
            for (int j = i + 2; j <= n; j += 2) {
                sum += j;
                if (sum == n) {
                    return true;
                }
            }
        }
        return false;
    }
}

