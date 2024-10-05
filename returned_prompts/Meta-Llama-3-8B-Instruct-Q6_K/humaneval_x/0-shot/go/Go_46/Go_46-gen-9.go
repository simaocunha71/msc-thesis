```go
func Fib4(n int) int {
    if n <= 3 {
        return 0
    }
    if n == 4 {
        return 2
    }
    a, b, c, d := 0, 0, 2, 2
    for i := 5; i <= n; i++ {
        a, b, c, d = b, c, d, a+b+c
    }
    return d
}
```


The solution uses a loop to calculate the n-th element of the Fib4 number sequence. It keeps track of the last four elements in the sequence and updates them in each iteration of the loop. This approach avoids the use of recursion and has a time complexity of O(n), making it efficient for large values of n. The base cases for n <= 3 are handled separately to simplify the code. The function returns the n-th element of the sequence.