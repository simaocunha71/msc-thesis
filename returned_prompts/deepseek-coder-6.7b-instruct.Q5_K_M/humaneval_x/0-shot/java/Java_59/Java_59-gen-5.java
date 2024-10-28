        int largest = -1;
        
        // Divide n by 2 until n becomes odd
        while (n % 2 == 0) {
            largest = 2;
            n >>= 1;
        }
        
        // n must be odd at this point, thus skip the even numbers and iterate only for odd
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                largest = i;
                n = n / i;
            }
        }
        
        // This condition is to handle the case when n is a prime number
        // greater than 2
        if (n > 2)
            largest = n;
        
        return largest;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.largestPrimeFactor(13195));  // Outputs 29
        System.out.println(sol.largestPrimeFactor(2048));  // Outputs 2
    }
}

Explanation:
The largest prime factor of a number can be found by continually dividing that number by the smallest possible prime number (starting from 2) until the number becomes 1. In this case, we check if the number is divisible by 2, and if it is, we divide it and update our largest prime factor. We then check for odd numbers (since all even numbers are divisible by 2). We continue this process until our number is greater than the square root of itself (since any factors of n will be less than or equal to sqrt(n)). If n is still greater than 2 after this process, it must be a prime number and we update our largest prime factor. Finally, we return our largest prime factor.
*/

// 13195 -> 29, 2048 -> 2.
// The largest prime factor of 13195 is 29, and the largest prime factor of 2048 is 2.

// The largest prime factor of a number is the largest prime number that divides the number evenly.
//