    // Given a positive integer n, return the count of the numbers of n-digit
    // positive integers that start or end with 1.

    // The count of n-digit numbers is 10^(n-1).
    // We need to subtract the count of n-digit numbers that start with 1 but end
    // with any number other than 1 (except 0) to get the count of n-digit
    // numbers that start or end with 1.

    // The count of n-digit numbers that