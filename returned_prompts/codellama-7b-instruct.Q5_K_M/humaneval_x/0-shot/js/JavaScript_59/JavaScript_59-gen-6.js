
// Brute force algorithm.

// Iterate from n/2 down to 2 to find the largest prime factor.
// Use a hash table to keep track of the prime factors and their exponents.

// Initialize hash table.
var primeFactors = {};

// Iterate from n/2 down to 2.
for (var i = n / 2; i >= 2; --i) {
    // If the current number is a prime factor of n.
    if (n % i === 0) {
        // If this is the first time we've seen this prime factor.
        if (!(i in primeFactors)) {
            // Set the exponent to 1.
            primeFactors[i] = 1;
        } else {
            // Increment the exponent.
            ++primeFactors[i];
        }
        // If we've found the largest prime factor, stop.
        if (primeFactors[i] === 1) {
            break;
        }
        // Try the next lower number.
        continue;
    }
    // If the current number is not a prime factor, try the next lower number.
    continue;
}

// Return the largest prime factor.
return i;

// Optimized algorithm.

// Iterate from n/2 down to 2 to find the largest prime factor.
// Use a hash table to keep track of the prime factors and their exponents.

// Initialize hash table.
var primeFactors = {};

// Iterate from n/2 down to 2.
for (var i = n / 2; i >= 2; --i) {
    // If the current number is a prime factor of n.
    if (n % i === 0) {
        // If this is the first time we've seen this prime factor.
        if (!(i in primeFactors)) {
            // Set the exponent to 1.
            primeFactors[i] = 1;
        } else {
            // Increment the exponent.
            ++primeFactors[i];
        }
        // If we've found the largest prime factor, stop.
        if (primeFactors[i] === 1) {