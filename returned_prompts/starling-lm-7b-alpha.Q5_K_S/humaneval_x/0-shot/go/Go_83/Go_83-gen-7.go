    // The number of one-digit positive integers that start or end with 1 is 2.
    if n == 1 {
        return 2
    }

    // For each digit, we have 10 choices.
    // There are n digits.
    // So, the total count is 10^n.
    total := math.Pow(10, float64(n))

    // However, we need to subtract the count of the numbers that start with 0.
    // For each digit, we have 9 choices.
    // There are n-1 digits.
    sub := math.Pow(9, float64(n-1))

    return int(total - sub)
}

































// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that start or end with 1.
func StartsOneEnds(n int) int {
    // The number of one-digit positive integers that start or end with 1 is 2.
    if n == 1 {
        return 2
    }

    // For each digit, we have 10 choices.
    // There are n digits.
    // So, the total count is 10^n.
    total := int(math.Pow(10, float64(n)))

    // However, we need to subtract the count of the numbers that start with 0.
    // For each digit, we have 9 choices.
    // There are n-1 digits.
    sub := int(math.Pow(9, float64(n-1)))

    return total - sub
}



// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that start or end with 1.
func StartsOneEnds(n int) int {
    // The number of one-digit positive integers that start or end with 1 is 2.
    if n == 1 {
        return 2
