
    // If number is less than 2, it's not prime.
    if n < 2 {
        return false
    }

B:

    // If number is 2, it's prime.
    if n == 2 {
        return true
    }

C:

    // If number is divisible by 2, it's not prime.
    if n % 2 == 0 {
        return false
    }

D:

    // Start checking from 3 to sqrt(n)
    for i := 3; i*i <= n; i += 2 {
        if n % i == 0 {
            return false
        }
    }

E:

    // If no divisor found, it's prime.
    return true
}

```

### 4. 斐波那契数列

```go
