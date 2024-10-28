        int largestFactor = 2; // 2 is the smallest prime number
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                largestFactor = i;
                n = n / i;
                while (n % i == 0) {
                    n = n / i;
                }
            }
        }
        if (n > 2) {
            largestFactor = n;
        }
        return largestFactor;
    }

Explanation:

The function `largestPrimeFactor` takes an integer `n` as input and returns the largest prime factor of `n`.

The function starts by initializing `largestFactor` to 2, which is the smallest prime number.

Then, it iterates over the numbers from 3 to the square root of `n` (inclusive) with a step of 2. For each number `i` in this range, it checks if `n` is divisible by `i` using the modulo operator `%`. If `n` is divisible by `i`, it means that `i` is a factor of `n`, and `largestFactor` is updated to `i`.

After updating `largestFactor`, the function divides `n` by `i` until `n` is no longer divisible by `i`. This is done to ensure that `n` is updated to its largest prime factor.

Finally, if `n` is greater than 2, it means that `n` is a prime number, and `largestFactor` is updated to `n`.

The function returns `largestFactor`, which is the largest prime factor of `n`.