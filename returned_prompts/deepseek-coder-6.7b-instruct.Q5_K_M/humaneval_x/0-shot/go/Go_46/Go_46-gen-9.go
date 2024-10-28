
// Solution:
// To solve this problem, we can use Dynamic Programming. We can initialize an array of size n+1 with the first four elements as per the given sequence. Then, we iterate from 4 to n, each time updating the ith element as the sum of (i-1)th, (i-2)th, (i-3)th and (i-4)th elements. Finally, the n-th element is the (n-1)th element of the array.

// Here is the Python code for the above approach:

```python
def Fib4(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    fib = [0]*n + [2] + [0]*(n-3)

    for i in range(4, n+1):
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4]

    return fib[n]
```

// And here is the equivalent code in Go:

```go
func Fib4(n int) int {
    if n == 0 {
        return 0
    }
    if n == 1 {
        return 0
    }
    if n == 2 {
        return 2
    }
    if n == 3 {
        return 0
    }

    fib := make([]int, n+1)
    copy(fib[4:], []int{0, 2, 0, 0})

    for i := 4; i <= n; i++ {
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4]
    }

    return fib[n]
}
```

// Both of these codes initialize an array with the first four elements as per the Fib4 sequence and then iterate from 4 to n, each time updating the ith element as the sum of (i-1)th, (i-2)