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
        Solution solution = new Solution();
        System.out.println(solution.largestPrimeFactor(13195)); // output: 29
        System.out.println(solution.largestPrimeFactor(2048)); // output: 2
    }
}

Explanation:
We start by dividing n by 2 until n becomes odd. This is because a composite number can always be factored into a product of prime numbers. If n is divisible by 2, it means the largest prime factor is 2. We then continue with the odd numbers only. We only need to check up to the square root of n because a larger factor of n must be a multiple of a smaller factor that has already been checked. If n is greater than 2 at the end, it means n is a prime number and we assign it as the largest prime factor.

Time complexity: O(sqrt(n))
Space complexity: O(1)
*/

// LeetCode Problem 507. Perfect Number
/*
