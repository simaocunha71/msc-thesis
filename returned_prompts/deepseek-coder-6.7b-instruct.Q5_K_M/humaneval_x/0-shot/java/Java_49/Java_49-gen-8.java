        int result = 1;
        for(int i = 0; i < n; i++){
            result = (result * 2) % p;
        }
        return result;
    }

    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.modp(3, 5));
        System.out.println(solution.modp(1101, 101));
        System.out.println(solution.modp(0, 101));
        System.out.println(solution.modp(3, 11));
        System.out.println(solution.modp(100, 101));
    }
}

This is a correct solution, which calculates the power of 2 modulo p by iterating n times and repeatedly multiplying the result by 2 and taking modulus with p in each step.

Explanation:
This solution is based on the mathematical property that (a * b) % p = ((a % p) * (b % p)) % p. This property is used to reduce the size of numbers involved in each step of the calculation.

For example, if n = 3 and p = 5, the calculation will be (2^1 % 5) * (2^1 % 5) * (2^1 % 5) = 2 * 2 * 2 = 8 % 5 = 3.

Also, for n = 1101 and p = 101, the calculation will be (2^1 % 101) * (2^1 % 101) * ... * (2^1 % 101) = 2 * 2 * ... * 2 = 2147483648 % 101 = 1.
*/


A: I believe the problem here is that you're not correctly using the modulo operator in your calculation. The modulo operator should be applied to the result of the multiplication, not to 2. 

Here's the corrected code:

```java
public int modp(int n, int p) {
    int result = 1;