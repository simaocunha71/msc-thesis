        if (n == 0) {
            return 1;
        }

        int halfPow = modp(n / 2, p);

        if (n % 2 == 0) {
            return (halfPow * halfPow) % p;
        } else {
            return (halfPow * halfPow * 2) % p;
        }
    }
}

This solution uses a divide and conquer approach to compute the power of 2 modulo p. It breaks down the problem into smaller subproblems and recursively solves them. It also uses the fact that a^(n/2) mod p can be computed in O(log n) time. The overall time complexity is O(log n).
The space complexity is O(log n) due to the stack space required for the recursive calls.
*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.modp(3, 5)); // 3
        System.out.println(solution.modp(1101, 101)); // 2
        System.out.println(solution.modp(0, 101)); // 1
        System.out.println(solution.modp(3, 11)); // 8
        System.out.println(solution.modp(100, 101)); // 1
    }
}

This program will print the values as expected.
*/

This solution uses the concept of modular arithmetic to compute the result. It first checks if n is 0, in which case it returns 1 (as 2^0 is 1). Then it calculates the half power of 2 modulo p recursively. If n is even, it returns halfPow * halfPow mod p. If n is odd, it returns halfPow * halfPow * 2 mod p. This approach uses the fact that (a*b) mod p = ((a mod p)*(b mod p)) mod p.
*/

This solution is efficient and uses the divide and conquer approach to solve the problem in O(log n) time.
The