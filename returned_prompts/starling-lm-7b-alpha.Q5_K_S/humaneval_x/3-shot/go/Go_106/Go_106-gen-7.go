    result := make([]int, n)
    for i := 1; i <= n; i++ {
        if i % 2 == 0 {
            result[i-1] = i
        } else {
            result[i-1] = sumRange(i)
        }
    }
    return result
}

func sumRange(n int) int {
    if n == 1 {
        return 1
    }
    return n + sumRange(n - 1)
}



