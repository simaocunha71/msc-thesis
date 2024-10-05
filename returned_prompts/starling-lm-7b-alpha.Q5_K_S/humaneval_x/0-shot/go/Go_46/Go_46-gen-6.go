
var f = make([]int, n + 1)
f[0] = 0
f[1] = 0
f[2] = 2
f[3] = 0

for i := 4; i <= n; i++ {
    f[i] = f[i-1] + f[i-2] + f[i-3] + f[i-4]
}

return f[n]
```

This is a classic problem of dynamic programming, which can be solved using array to store the intermediate results. In this problem, we can find the n-th element of the Fib4 number sequence, just by calculating it in order.

```go
var f = make([]int, n + 1)
f[0] = 0
f[1] = 0
f[2] = 2
f[3] = 0

for i := 4; i <= n; i++ {
    f[i] = f[i-1] + f[i-2] + f[i-3] + f[i-4]
}

return f[n]
```

For example, if we want to calculate Fib4(5), we first set f[0] = 0, f[1] = 0, f[2] = 2, f[3] = 0. Then, we calculate f[4] = f[3] + f[2] + f[1] + f[0] = 0 + 2 + 0 + 0 = 2. Next, we calculate f[5] = f[4] + f[3] + f[2] + f[1] = 2 + 0 + 2 + 0 = 4. Finally, we calculate f[6] = f[5] + f[4] + f[3] + f[2] = 4 + 2 + 0 + 2 = 8, which is the Fib4(6) value.

To calculate Fib4(7), we can follow the same process, and we can get the result 14.

```
func Fib4(n int) int {
    var f = make([]int