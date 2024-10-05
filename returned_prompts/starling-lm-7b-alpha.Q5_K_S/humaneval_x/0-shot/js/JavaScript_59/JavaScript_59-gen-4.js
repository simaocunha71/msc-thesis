    let maxFactor = -1;
    while (n % 2 === 0) {
        maxFactor = 2;
        n /= 2;
    }

    for (let i = 3; i <= Math.sqrt(n); i += 2) {
        while (n % i === 0) {
            maxFactor = i;
            n /= i;
        }
    }

    if (n > 2) {
        maxFactor = n;
    }

    return maxFactor;
};

largestPrimeFactor(13195);

*/

In this code, the `largestPrimeFactor` function takes a number `n` as input and returns the largest prime factor of `n`. It first checks if `n` is divisible by 2 and repeatedly divides `n` by 2 until it is no longer divisible by 2. Then, it uses a for loop to check if `n` is divisible by odd numbers starting from 3 up to the square root of `n`. If `n` is divisible by an odd number `i`, it repeatedly divides `n` by `i` until it is no longer divisible by `i`. Finally, if `n` is greater than 2, it means that `n` itself is a prime number, so the function returns `n`.

To use this function, you can call `largestPrimeFactor` with a number as an argument, like `largestPrimeFactor(13195)` or `largestPrimeFactor(2048)`. The function will then return the largest prime factor of the given number.

For example, if you call `largestPrimeFactor(13195)`, the function will return 29, as 29 is the largest prime factor of 13195. If you call `largestPrimeFactor(2048)`, the function will return 2, as 2 is the largest prime factor of 2048.

This function is useful when you need to find the largest prime factor of a given number in JavaScript.



























