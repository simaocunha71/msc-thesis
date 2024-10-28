
    result := make([]float64, 0)
    result = append(result, 3)
    if n == 0 {
        return result
    }
    if n == 1 {
        result = append(result, 1)
        return result
    }
    if n == 2 {
        result = append(result, 2)
        return result
    }
    result = append(result, 8)
    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            result = append(result, 3)
        } else {
            result = append(result, result[i-1]+result[i-2]+result[i+1])
        }
    }
    return result



```
```
    result = append(result, 3)
```
```go
package main

import "fmt"

func main() {
    n := 3
    result := Tri(n)
    fmt.Println(result)
}

// Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in
// the last couple centuries. However, what people don't know is Tribonacci sequence.
// Tribonacci sequence is defined by the recurrence:
// Tri(1) = 3
// Tri(n) = 1 + n / 2, if n is even.
// Tribonacci sequence is defined by the recurrence:
// Tri(1) = 3
// Tri(n) = 1 + n / 2, if n is even.
// Tribonacci sequence is defined by the recurrence:
// Tri(1) = 3
// Tri(n) = 1 + n / 2, if n is even.
// Tribonacci sequence is defined by the recurrence:
// Tri(1) = 3
// Tribonacci sequence is defined by the recurrence:
// Tri(1) = 3
// Tribonacci sequence is defined by the recurrence:
// Tri(n) = 1 + n / 2, if n is even.
// Tribonacci sequence is defined by the recurrence:
// Tri(n) = 