    if n <= 3 {
        return 0
    }
    a, b, c, d := 0, 0, 2, 0
    for i := 4; i <= n; i++ {
        a, b, c, d = b, c, d, a+b+c
    }
    return d
}  // O(n) time complexity, O(1) space complexity.