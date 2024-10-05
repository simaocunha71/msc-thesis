        List<Integer> factors = new ArrayList<>();

        // Divide n by 2 until n becomes odd
        while (n % 2 == 0) {
            factors.add(2);
            n = n / 2;
        }

        // n is now odd, so find odd factors of n
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                factors.add(i);
                n = n / i;
            }
        }

        // This condition is to handle the case when n is a prime number greater than 2
        if (n > 2) {
            factors.add(n);
        }

        return factors;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.factorize(8)); // should print [2, 2, 2]
        System.out.println(solution.factorize(25)); // should print [5, 5]
        System.out.println(solution.factorize(70)); // should print [2, 5, 7]
    }
}

The algorithm works by dividing the given number by 2 until it becomes odd. Then it finds other factors by dividing the number by odd numbers starting from 3. If the remaining number is greater than 2, it means that number itself is a prime number and it is added to the list. The factors are returned in the list in the order from smallest to largest.

This algorithm works because all prime numbers are of the form 6k ± 1, for some k, except for 2 and 3. Therefore, a larger factor of the number must be a multiple of 6k ± 1, and must have already been discovered by the point the number is divided by 2.

The time complexity of this algorithm is O(sqrt(n)), where n is the number to be factorized. This is because the loop runs until the square root of the number.
The space complexity is also O(sqrt(n)), because in the worst case, the number of factors is proportional to the square root of the number.

The