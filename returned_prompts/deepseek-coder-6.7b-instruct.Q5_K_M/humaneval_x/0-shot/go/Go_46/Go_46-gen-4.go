
// Initialize base cases
fib4 := make([]int, n+1)
fib4[0] = 0
if n > 0 {
    fib4[1] = 0
}
if n > 1 {
    fib4[2] = 2
}
if n > 2 {
    fib4[3] = 0
}

// Compute the sequence up to n
for i := 4; i <= n; i++ {
    fib4[i] = fib4[i-1] + fib4[i-2] + fib4[i-3] + fib4[i-4]
}

return fib4[n]

B:

}



