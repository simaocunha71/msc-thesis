    var (
        n0 = n
        res []int
    )
    for i := 2; i <= math.Sqrt(float64(n)); i++ {
        for n != 0 && n%i == 0 {
            res = append(res, i)
            n /= i
        }
    }
    if n != 0 {
        res = append(res, n)
    }
    return res
}





I'm using this code to get the prime factors of a number, but when I run it, I get an error: `cannot use n0 (type int) as type float64 in function argument` in the for loop.

Here is how I'm calling the function:

```go
fmt.Println(Factorize(8))
```

It seems like the function is expecting a float64 instead of an int. Why is that and how can I fix it?

The function works fine with an int, so the error message is misleading. It's probably a bug in the Go compiler.

To fix the problem, you can cast the value of `n0` to a float64 in the for loop, like this:

```go
for i := 2; i <= math.Sqrt(float64(n0)); i++ {
    // ...
}
```

This will ensure that the `math.Sqrt` function receives a float64 value, and the code will compile without errors.

However, it's worth noting that the error message is incorrect. The `math.Sqrt` function actually accepts an int64 input, so there's no need to cast `n0` to a float64 in this case. The issue seems to be a bug in the Go compiler, which incorrectly reports an error when using `math.Sqrt` with an int64 value.

To confirm this, you can try casting `n0` to an int64 instead of a float64, like this:

```go
for i := 2; i <= math.Sqrt(int64(n0)); i++ {
    // ...
}
```

This should also work correctly