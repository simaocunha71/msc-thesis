    let limit = Math.floor(n / 2) + 1;
    let i = 3;
    while (i <= limit) {
        while (n % i === 0) {
            n /= i;
            limit = Math.floor(n / 2) + 1;
        }
        i += 2;
    }
    return n;
};

The above code defines a function called `largestPrimeFactor` that takes an integer `n` as input and returns the largest prime factor of `n`. Here's a breakdown of the code:

1. The variable `limit` is initialized with the value of `Math.floor(n / 2) + 1`. This value is used as an upper limit for the factors of `n` that we will check.

2. The variable `i` is initialized with the value `3`, which is the smallest prime number. We start checking factors from this number because even numbers are not prime and we can skip them.

3. The while loop `while (i <= limit)` is used to iterate through all the potential factors of `n`. In each iteration, we check if `n` is divisible by `i` using the condition `while (n % i === 0)`. If it is divisible, we divide `n` by `i` and update the value of `limit` to `Math.floor(n / 2) + 1`. This is done to ensure that we only consider factors less than or equal to the updated limit.

4. After the inner while loop, we increment the value of `i` by `2` to move on to the next potential factor. We increment by `2` because all even numbers greater than `2` are not prime.

5. The outer while loop continues until `i` becomes greater than `limit`, at which point the function returns the value of `n`. Since `n` is the largest prime factor that is greater than `limit`, it is the largest prime factor of the original input `n`.

In the given code, the function `largestPrimeFactor` is tested with two examples: `largestPrimeFactor(13195)` and `largestPrimeFactor(2048)`. The expected outputs for these examples are `2