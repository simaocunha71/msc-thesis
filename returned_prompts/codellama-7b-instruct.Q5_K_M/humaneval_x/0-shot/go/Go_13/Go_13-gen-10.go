
// Return a greatest common divisor of two integers a and b
// >>> GreatestCommonDivisor(3, 5)
// 1
// >>> GreatestCommonDivisor(25, 15)
// 5
func GreatestCommonDivisor(a int,b int) int{

    // Swap a and b if a < b
    if a < b {
        a, b = b, a
    }

    // Loop until b is 0
    for b != 0 {
        // Swap a and b
        a, b = b, a

        // Subtract b from a
        a = a % b
    }

    // Return a
    return a
}
