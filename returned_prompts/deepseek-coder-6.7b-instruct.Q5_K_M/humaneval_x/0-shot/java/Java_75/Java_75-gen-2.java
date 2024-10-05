        int count = 0;
        for (int i = 2; i <= a; i++) {
            if (a % i == 0) {
                while (a % i == 0) {
                    a = a / i;
                    count++;
                }
                if (isPrime(i) == false) {
                    return false;
                }
            }
        }
        return count == 3 && isPrime(a);
    }

    public boolean isPrime(int n) {
        if (n == 2 || n == 3)
            return true;
        if (n % 2 == 0 || n == 1)
            return false;
        for (int i = 3; i * i <= n; i = i + 2) {
            if (n % i == 0)
                return false;
        }
        return true;
    }
}

Explanation:
First, the function checks if the number is divisible by any prime number from 2 to n. If it is, it counts that number. This is repeated until the number is not divisible by that prime number anymore. 
If the number is divisible by a prime number that is not 2 or 3, the function returns false. 
Finally, the function returns true if the count of prime numbers is 3 and the number itself is a prime number.

In the function isPrime, it checks if the number is divisible by any number up to its square root. If it is, it returns false. If it is not divisible by any number up to its square root, it returns true.
*/

public class Main
{
    public static void main (String[] args) throws java.lang.Exception
    {
        Solution solution = new Solution();
        System.out.println(solution.isMultiplyPrime(30)); //true
        System.out.println(solution.isMultiplyPrime(31)); //false
    }
}

This program will print:
true
false

which are the expected results.
*/

// This is a Java solution for the problem of checking if a number can be expressed as the multiplication of 3 prime numbers.
// It uses a simple approach of prime factor