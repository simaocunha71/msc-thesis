    if n <= 3 {
        return []int{0, 0, 2, 0}[n-1]
    }
    fib4 := [4]int{0, 0, 2, 0}
    for i := 4; i <= n; i++ {
        fib4[i%4] = (fib4[(i-1)%4] + fib4[(i-2)%4] + fib4[(i-3)%4]) % 4
    }
    return fib4[n%4]
}