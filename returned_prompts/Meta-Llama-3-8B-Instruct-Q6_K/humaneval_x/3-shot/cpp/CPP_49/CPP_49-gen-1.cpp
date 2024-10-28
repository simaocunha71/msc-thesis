    return (int)pow((double)n, (double)p) % p;
} // Warning: This may cause overflow or underflow for large values of n and p
// Also, this implementation is not the most efficient, as it uses pow and then mod, which is slower than the correct implementation
// Correct implementation would be to use exponentiation by squaring, and then mod. But the given code is simple and easy to understand.