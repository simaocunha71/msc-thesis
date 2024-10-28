    // Initialize the result variable
    result := 1

    // Loop through the bits of n from right to left
    for n > 0 {
        // If the current bit is 1, multiply the result by p
        if n % 2 == 1 {
            result = (result * p) % p
        }
        // Divide n by 2
        n = n / 2
    }
    return result
}
```

In this Python code, the function Modp(n, p) calculates 2^n modulo p. It does so by using a loop to iterate over the bits of n from right to left. If the current bit is 1, it multiplies the current result by p and takes the modulus with p. It then divides n by 2. This process is repeated until n becomes 0. The final result is returned.

Please note that the variable p should be a prime number for this function to work correctly. If p is not a prime number, the function may return incorrect results due to the properties of modular arithmetic. Also, the function assumes that n is a non-negative integer. If n is negative, the function will return incorrect results.