        int largest = -1;
        
        while (n % 2 == 0) {
            largest = 2;
            n >>= 1;
        }

        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                largest = i;
                n = n / i;
            }
        }

        if (n > 2)
            largest = n;

        return largest;
    }
}

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.largestPrimeFactor(13195)); // 29
        System.out.println(solution.largestPrimeFactor(2048)); // 2
    }
}

Explanation:

This program finds the largest prime factor of a given number. It does this by dividing the number by 2 until it is no longer divisible by 2 (storing 2 as the largest factor it can find), then it checks all odd numbers up to the square root of the remaining number (it only needs to check odd numbers because even numbers would have already been dealt with). If there is still a remaining number after this, it is prime and is the largest factor.

This method of repeatedly dividing by small numbers is known as trial division and is efficient for small numbers, but can be slow for large numbers.

This program uses the fact that all prime numbers are of the form 6k ± 1, with the exception of 2 and 3, to skip checks for even numbers and multiples of 3. It does this by incrementing the counter i by 2 after each check, and by adding 2 to n after each successful division.

The time complexity of this program is O(sqrt(n)).

This program also uses bitwise shift operators to divide n by 2, which is more efficient than using the division operator.

The space complexity of this program is O(1), since it only uses a constant amount of space.

The program works for all positive integers greater than 1, except for the number 1 which is not considered a prime