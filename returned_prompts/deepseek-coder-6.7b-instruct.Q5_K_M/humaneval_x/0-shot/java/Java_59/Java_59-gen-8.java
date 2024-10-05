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

    public static void main (String[] args) throws java.lang.Exception {
        // your code goes here
        System.out.println(new Solution().largestPrimeFactor(13195)); // 29
        System.out.println(new Solution().largestPrimeFactor(2048)); // 2
    }
}

In the provided solution, the function largestPrimeFactor checks if the number is divisible by 2 and if so, it keeps dividing by 2 until it is not divisible by 2. Then it checks for odd numbers only and checks if the number is divisible by these numbers. If it is divisible, it keeps dividing and keeps track of the largest number that it is divisible by. If the number is not divisible by any of these numbers, it is a prime number and it is the largest prime factor. 

The time complexity of this solution is O(sqrt(n)) which is the best possible time complexity for this problem.

The space complexity of this solution is O(1) because it uses a fixed amount of space.

This solution works for all numbers greater than 1 and not prime.
*/

// DO NOT EDIT BELOW THIS LINE

public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.largestPrimeFactor(13195)); // Expected output: 29
    System.out.println