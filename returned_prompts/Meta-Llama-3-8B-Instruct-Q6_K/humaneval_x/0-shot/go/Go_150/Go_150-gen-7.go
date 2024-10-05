    // Your code here
    // Check if n is prime
    if n <= 1 {
        return y
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return y
        }
    }
    return x
}

Solutions:

Solution 1:

```go
package main

import (
    "fmt"
    "math"
)

func XOrY(n, x, y int) int {
    // Check if n is prime
    if n <= 1 {
        return y
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return y
        }
    }
    return x
}

func main() {
    fmt.Println(XOrY(7, 34, 12)) // Output: 34
    fmt.Println(XOrY(15, 8, 5))  // Output: 5
}
```

Solution 2:

```go
package main

import (
    "fmt"
)

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func XOrY(n, x, y int) int {
    if isPrime(n) {
        return x
    }
    return y
}

func main() {
    fmt.Println(XOrY(7, 34, 12)) // Output: 34
    fmt.Println(XOrY(15, 8, 5))  // Output: 5
}
```

Solution 3:

```go
package main

import (
    "fmt"
)

func XOrY(n, x, y int) int {
    if isPrime(n) {
        return x
    }
    return y
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(XOrY(7, 34, 12)) // Output: 34
    fmt.Println(XOrY(15