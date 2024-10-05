    sum := 0
    for i := 1; i <= n; i++ {
        sum += i
    }
    return sum
} // This function is not efficient for large numbers. For larger numbers, the formula sum = n*(n+1)/2 can be used.