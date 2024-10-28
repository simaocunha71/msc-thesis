    if n <= 1 {
        return false
    }
    for i := 2; i <= math.Sqrt(float64(n)); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}  // O(n^(1/2)) time complexity. This is the most efficient algorithm for checking primality.  // It's worth noting that this algorithm can be further optimized by using a prime number table.