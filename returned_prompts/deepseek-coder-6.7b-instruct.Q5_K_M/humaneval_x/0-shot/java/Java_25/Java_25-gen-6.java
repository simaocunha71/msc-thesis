        List<Integer> factors = new ArrayList<>();

        // Divide n by 2 until n becomes odd
        while (n % 2 == 0) {
            factors.add(2);
            n /= 2;
        }

        // n must be odd at this point so a skip of 2 can be used
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }

        // This condition is to handle the case when n is a prime number
        // greater than 2
        if (n > 2) {
            factors.add(n);
        }

        return factors;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.factorize(8)); // [2, 2, 2]
        System.out.println(solution.factorize(25)); // [5, 5]
        System.out.println(solution.factorize(70)); // [2, 5, 7]
    }
}

In this solution, we are using the fact that all numbers can be represented as product of primes. We keep dividing the number by 2 until we get an odd number. After that, we start dividing by 3 and continue till the square root of the number. If the number is still greater than 2 after this, we add it to the list as it is a prime number. 

Also, to make the process quicker, we only check divisors up to the square root of the number, as any factors beyond that would have already been covered.

The time complexity of this solution is O(sqrt(n)).

It should be noted that the order in which the factors are returned does not matter, as long as they are all there and the correct number of times.

Also, the input number should be equal to the product of all factors. This is not checked in this solution.

The main method in the solution class tests the factorize method with the three examples given in the question.

The space complexity of this solution