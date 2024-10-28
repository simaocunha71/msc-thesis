
// 1. Base case: if n is 0 or 1, return n itself
if n <= 1 {
    return n
}

// 2. Recursive case: return the sum of the (n-1)th and (n-2)th Fibonacci number
return Fib(n-1) + Fib(n-2)

}
```

This solution works well for small inputs. However, it has exponential time complexity due to the redundant calculations in the recursive calls. For larger inputs, it will be slow. To optimize, we can use dynamic programming to store the previously computed Fibonacci numbers and use them in the subsequent calculations.

Here is the optimized solution:

```go
func Fib(n int) int {
    // Initialize a slice to store the Fibonacci numbers.
    // The slice is initialized with the first two Fibonacci numbers.
    fib := []int{0, 1}

    // Append the next Fibonacci numbers to the slice until we reach the nth Fibonacci number.
    for i := 2; i <= n; i++ {
        fib = append(fib, fib[i-1]+fib[i-2])
    }

    // Return the nth Fibonacci number.
    return fib[n]
}
```

This solution has linear time complexity and is much more efficient for larger inputs.

## 2. Array Rotation

