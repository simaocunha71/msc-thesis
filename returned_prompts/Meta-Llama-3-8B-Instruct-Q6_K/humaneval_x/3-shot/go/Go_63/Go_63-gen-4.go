    if n <= 1 {
        return 0
    }
    if n == 2 {
        return 1
    }

    var a, b, c int = 0, 0, 1
    for i := 3; i <= n; i++ {
        a, b, c = b, c, a+b+c
    }
    return c
}  // O(n) time complexity, O(1) space complexity.