    long long result = 1;
    for (int i = n; i > 0; i--) {
        result *= i;
        for (int j = i - 1; j > 0; j--) {
            result *= j;
        }
    }
    return result;
}
// This function will return the special factorial of the input integer. It uses two nested loops to calculate the result. The outer loop starts from the input integer and goes down to 1, and the inner loop starts from the current integer and goes down to 1. The result is calculated by multiplying the product of all integers from the current integer down to 1 with the product of all integers from the current integer down to 1. The result is then returned as the special factorial of the input integer.
// The function returns the result as a long long integer, which is a 64-bit integer type that can store large numbers. This is necessary because the special factorial can grow very large for large input integers. For example, the special factorial of 20 is 2432902008176640000, which is a 20-digit number. The function uses the long long integer type to handle such large numbers.