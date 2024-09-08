    // Calculate 2^n mod p using exponentiation by squaring
    int result = 1;
    while (n > 0) {
        if (n % 2 == 1) {
            result = (result * p) % p;
        }
        n = n / 2;
        p = (p * p) % p;
    }
    return result;
}

B:
    return pow(2, n) % p;  // use math library's pow function
}
C:
    return (1 << n) % p;  // left shift operation
}
D:
    // Calculate 2^n mod p using recursion
    if (n == 0) {
        return 1;
    } else {
        int temp = modp(n / 2, p);
        if (n % 2 == 1) {
            return (temp * p) % p;
        } else {
            return temp * temp % p;
        }
    }
}E:
    return (int)pow(2.0, n) % p;  // use math library's pow function with double

Explanation:
The correct answer is A. This problem asks to calculate 2^n modulo p, and the most efficient way to do this is using exponentiation by squaring. This method is more efficient than using recursion or the math library's pow function, especially for large values of n.

The code in answer A calculates 2^n mod p by repeatedly squaring p and multiplying the result by the current value of 2^n, if n is odd. This method has a time complexity of O(log n), making it much faster than the other options.

The code in answer B uses the math library's pow function, which is not the most efficient way to calculate 2^n mod p. This method has a time complexity of O(n), making it slower than answer A for large values of n.

The code in answer C uses the left shift operation, which is not the most efficient way to calculate 2^n mod p. This method has a time complexity of O(n), making it slower than answer A for large values of n.

The code in answer D uses recursion, which is not the most efficient way to calculate 2^n mod p. This method has a time complexity of O(n), making it slower than answer A for large values of n.

The code in answer E uses the math library's pow function with a double, which is not the most