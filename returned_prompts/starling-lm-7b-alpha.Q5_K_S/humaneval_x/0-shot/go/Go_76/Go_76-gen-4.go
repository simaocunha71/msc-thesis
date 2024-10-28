
```go
var logX int
var logN int

for x > 1 {
    logX++
    x /= n
}

for n > 1 {
    logN++
    n /= n
}

if logX == logN {
    return true
} else {
    return false
}
```

Explanation:

The function counts the number of times n divides x until x becomes 1 (logX). Then it counts the number of times n divides n until n becomes 1 (logN). If logX == logN then x is a simple power of n and the function returns true, otherwise it returns false.

```go
func IsSimplePower(x int,n int) bool {
    var logX int
    var logN int

    for x > 1 {
        logX++
        x /= n
    }

    for n > 1 {
        logN++
        n /= n
    }

    if logX == logN {
        return true
    } else {
        return false
    }
}
```

This solution has O(logN) complexity, where N is the value of x.

```go
func IsSimplePower(x int,n int) bool {
    var logX int
    var logN int

    for x > 1 {
        logX++
        x /= n
    }

    for n > 1 {
        logN++
        n /= n
    }

    if logX == logN {
        return true
    } else {
        return false
    }
}
```

This solution has O(logN) complexity, where N is the value of x.

```go
func IsSimplePower(x int,n int) bool {
    var logX int
    var logN int

    for x > 1 {
        logX++
        x /= n
    }

    for n > 1 {
        logN++
        n /= n
    }

    if logX == logN {
        return true
    } else {
        return false
