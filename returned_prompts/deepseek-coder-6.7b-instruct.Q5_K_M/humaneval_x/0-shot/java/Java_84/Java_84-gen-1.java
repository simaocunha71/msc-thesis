        String binary = Integer.toBinaryString(N);
        int sum = 0;
        for (char c : binary.toCharArray()) {
            sum += Character.getNumericValue(c);
        }
        return Integer.toBinaryString(sum);
    }

}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solve(1000));  // 1
        System.out.println(sol.solve(150));   // 110
        System.out.println(sol.solve(147));   // 1100
    }
}


This code takes an integer N as input, converts it to binary, then iterates over each character in the binary string, converting each character to its numeric value and adding them all together. The resulting sum is then converted back to binary and returned.

*/

import java.util.*;
import java.lang.*;

class Solution {
    public String solve(int N) {
        String binary = Integer.toBinaryString(N);
        int sum = 0;
        for (char c : binary.toCharArray()) {
            sum += Character.getNumericValue(c);
        }
        return Integer.toBinaryString(sum);
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solve(1000));  // 1
        System.out.println(sol.solve(150));   // 110
        System.out.println(sol.solve(147));   // 1100
    }
}import java.util.*;

public class Main {
    public static void main(String[] args) {
        System.out.println(solve(1000));  // 1
        System.out.println(solve(150));   // 6
        System.out.println(solve(147));   // 12
    }

