        if(n <= 1) {
            return false;
        }
        if(n == 2) {
            return true;
        }
        if(n % 2 == 0) {
            return false;
        }
        for(int i = 3; i * i <= n; i += 2) {
            if(n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

This solution works by first checking if the number is less than or equal to 1, in which case it's not prime. Then it checks if the number is 2, which is prime. If the number is even and not 2, it's not prime.

Then it checks all possible divisors from 3 up to the square root of the number. If the number is divisible by any of these, it's not prime. If it doesn't find any divisors, it's prime.

The reason we only need to check up to the square root of the number is that a larger factor of the number would be a multiple of a smaller factor that has already been checked.

The time complexity of this solution is O(sqrt(n)).

Note: This solution assumes that the input number is non-negative. If the input number could be negative, you would need to add additional checks to handle that case.
*/

//Test cases
public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.isPrime(6)); // false
        System.out.println(s.isPrime(101)); // true
        System.out.println(s.isPrime(11)); // true
        System.out.println(s.isPrime(13441)); // false
        System.out.println(s.isPrime(61)); // true
        System.out.println(s.isPrime(4)); // false
        System.out.println(s.isPrime(1)); // false
    }
}

//Test cases
public class Main {
    public static void main (String[] args) throws java.