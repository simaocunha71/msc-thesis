        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                primes.add(i);
            }
        }
        return primes;
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

// the function isPrime checks whether a given number is a prime number or not. It does so by
// iterating from 2 to that number and checking if the number is divisible by any of these numbers.
// If it is, then the number is not a prime number. If it is not divisible by any of these numbers,
// then the number is a prime number.

// the function countUpTo checks all the numbers up to the given number and adds them to the
// list if they are prime numbers. It does so by using the function isPrime.

// the time complexity of this function is O(n^2) as the function isPrime is called n times, and
// for each call, it iterates up to the number. Therefore, the time complexity is O(n^2).

// the space complexity of this function is O(n) because it stores all the prime numbers up to n.
// Therefore, the space complexity is O(n).

// this solution is not efficient for large inputs as the time complexity is high. A more efficient
// solution would use the Sieve of Eratosthenes algorithm to find all prime numbers up to n in O(n log log n)
// time.

// the Sieve of Eratosthenes works by iteratively marking the multiples of numbers, starting from 2.
// The multiples of a given number are generated as a sequence of numbers starting from that number,
// with a constant difference between them. This difference is equal to that number. This is the key
// distinction between this algorithm and the Sieve of Atkin.

// the Sieve of Eratost