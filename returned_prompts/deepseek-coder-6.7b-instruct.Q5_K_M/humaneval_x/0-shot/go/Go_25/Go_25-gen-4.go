    var factors []int

    for i := 2; i <= int(math.Sqrt(float6Wh(n))); i++ {
        for n%i == 0 {
            factors = append(factors, i)
            n = n / i
        }
    }

    if n > 1 {
        factors = append(factors, n)
    }

    return factors
}
```

## 2. Prime Number Check

This function checks whether a given number is prime or not.

```go
