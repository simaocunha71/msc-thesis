    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i%2 == 0 {
            result[i] = factorial(i)
        } else {
            result[i] = sumToN(i)
        }
    }
    return result
}

func factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * factorial(n-1)
}

func sumToN(n int) int {
    if n == 0 {
        return 0
    }
    return n + sumToN(n-1)
}

// Test Cases
// F(5) == [1, 2, 6, 24, 15]
// F(1) == [1]
// F(0) == []



