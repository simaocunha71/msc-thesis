当然可以，我们可以通过只计算斐波那契数列中素数的部分来提高效率。我们可以使用一个循环来生成斐波那契数列，同时检查每个数是否为素数。如果是素数，我们就将其添加到结果列表中。这种方法可以避免在计算斐波那契数列的过程中进行不必要的素数检查。

以下是优化后的代码：

```go
func PrimeFib(n int) int {
    fib := []int{2, 3}
    i := 2
    for len(fib) < n {
        i++
        if isPrime(fib[i-1] + fib[i-2]) {
            fib = append(fib, fib[i-1] + fib[i-2])
        }
    }
    return fib[n-1]
}

func isPrime(num int) bool {
    if num <= 1 {
        return false
    }
    for i := 2; i*i <= num; i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}
```

在这个优化后的版本中，我们只生成斐波那契数列中素数的部分，这样可以避免进行不必要的素数检查，从而提高效率。

希望这个优化方法对你有帮助！