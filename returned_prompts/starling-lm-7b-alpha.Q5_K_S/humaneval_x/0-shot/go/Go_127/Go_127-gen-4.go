    // Check whether two intervals intersect
    if interval1[0] > interval2[1] || interval2[0] > interval1[1] {
        return "NO"
    }
    // Calculate the length of intersection
    left, right := max(interval1[0], interval2[0]), min(interval1[1], interval2[1]);
    length := right - left + 1
    if isPrime(length) {
        return "YES"
    }
    return "NO"
}

func isPrime(n int) bool {
    if n == 1 {
        return false
    }
    for i := 2; i * i <= n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

```

Here's a solution in Go to the Intersection problem.

```go
package main

import "fmt"

func Intersection(interval1, interval2 [2]int) string {
    // Check whether two intervals intersect
    if interval1[0] > interval2[1] || interval2[0] > interval1[1] {
        return "NO"
    }
    // Calculate the length of intersection
    left, right := max(interval1[0], interval2[0]), min(interval1[1], interval2[1]);
    length := right - left + 1
    if isPrime(length) {
        return "YES"
    }
    return "NO"
}

func isPrime(n int) bool {
    if n == 1 {
        return false
    }
    for i := 2; i * i <= n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func max(a, b int) int {
   