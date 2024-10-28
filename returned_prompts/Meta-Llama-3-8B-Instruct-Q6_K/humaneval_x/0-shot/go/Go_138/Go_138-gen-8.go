```go
func IsEqualToSumEven(n int) bool {
    for i := 2; i <= n; i += 2 {
        for j := 2; j <= n; j += 2 {
            for k := 2; k <= n; k += 2 {
                for l := 2; l <= n; l += 2 {
                    if i+j+k+l == n {
                        return true
                    }
                }
            }
        }
    }
    return false
}
```

B:
```go
func IsEqualToSumEven(n int) bool {
    for i := 2; i <= n; i += 2 {
        for j := 2; j <= n; j += 2 {
            if i+j >= n {
                break
            }
            for k := 2; k <= n; k += 2 {
                if i+j+k >= n {
                    break
                }
                for l := 2; l <= n; l += 2 {
                    if i+j+k+l == n {
                        return true
                    }
                }
            }
        }
    }
    return false
}
```

C:
```go
func IsEqualToSumEven(n int) bool {
    for i := 2; i <= n; i += 2 {
        if i > n-i {
            break
        }
        for j := 2; j <= n; j += 2 {
            if i+j > n-i-j {
                break
            }
            if i+j > n-i-j {
                continue
            }
            k := n - i - j
            if k > 0 && k%2 == 0 {
                return true
            }
        }
    }
    return false
}
```

D:
```go
func IsEqualToSumEven(n int) bool {
    for i := 2; i <= n; i += 2 {
        for j := 2; j <= n; j += 2 {
            for k := 2; k <= n; k += 2 {
                for l := 2; l <= n; l += 2 {
                    if i+j+k+l == n && i <= j && j <= k && k <= l {
                        return true
                    }
                }
            }
        }
    }
    return false
}
```

The correct answer is C:
```go
func IsEqualToSumEven(n int) bool {
    for i :=