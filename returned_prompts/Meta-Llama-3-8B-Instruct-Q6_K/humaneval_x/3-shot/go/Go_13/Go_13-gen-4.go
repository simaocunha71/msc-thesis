    if b == 0 {
        return a
    }
    return GreatestCommonDivisor(b, a % b)
} // This is a recursive function to find the greatest common divisor of two numbers. It uses the Euclidean algorithm, which is an efficient method to find the GCD of two numbers. The idea is to replace 'a' with 'b' and 'b' with the remainder of 'a' divided by 'b', until 'b' becomes 0. The GCD of 'a' and 'b' is then 'a'.