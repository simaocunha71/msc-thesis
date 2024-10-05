    count := 0
    for i := 1; i <= 9; i++ {
        count += 1
        if i < 10 {
            count += 1
        }
    }
    return count
} // No, this is incorrect. The correct solution is:
    // let's consider the following cases:
    // - the number starts with 1 and ends with 1
    // - the number starts with 1 but does not end with 1
    // - the number does not start with 1 but ends with 1
    // - the number does not start with 1 and does not end with 1
    // the number of n-digit numbers that start with 1 and end with 1 is 9 * 1
    // the number of n-digit numbers that start with 1 but do not end with 1 is 9 * (10^(n-1) - 1)
    // the number of n-digit numbers that do not start with 1 but end with 1 is 9 * (10^(n-1) - 1)
    // the number of n-digit numbers that do not start with 1 and do not end with 1 is 8 * (10^(n-1) - 1)
    // so the total number is 9 * 1 + 9 * (10^(n-1) - 1) + 9 * (10^(n-1) - 1) + 8 * (10^(n-1) - 1)
    // which is 9 * (10^(n-1) + 1)
    return int(math.Pow(10, float64(n-1))) + 9
} // This is the correct solution. It calculates the number of n-digit numbers that start or end with 1.