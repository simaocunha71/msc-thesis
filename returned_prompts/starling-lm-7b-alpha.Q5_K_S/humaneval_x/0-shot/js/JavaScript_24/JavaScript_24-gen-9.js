    let i = 2;
    while (i * i <= n) {
        if (n % i == 0) {
            return i;
        }
        i++;
    }
    return n;
};

/* For a given number n, find the largest number that divides n evenly, smaller than n
  >>> largestDivisor(15)
  5
  */
const largestDivisor = (n) => {
    let i = 2;
    while (i * i <= n) {
        if (n % i == 0) {
            return i;
        }
        i++;
    }
    return n;
};

// Test
console.log(largestDivisor(15)); // 5

// Explanation:
/* Here, we use a while loop to check all the numbers up to square root of n (i * i <= n).
If the number is a divisor of n, we return that number. Otherwise, we increment i by 1 and
check the next number. If none of the number is a divisor, we return n itself. */

The time complexity of this approach is O(√n) as we only need to check the numbers up to square root of n.

Here is a simple JavaScript function that implements this idea:


















































































































































































































