    if n <= 3 {
        return 0
    } else if n == 4 {
        return 2
    }
    fib4 := [5]int{0,0,2,0,2}
    for i := 5; i <= n; i++ {
        fib4[i%5] = (fib4[(i-1)%5] + fib4[(i-2)%5] + fib4[(i-3)%5] + fib4[(i-4)%5]) % 10
    }
    return fib4[n%5]
}