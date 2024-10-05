```go
package main

import (
    "fmt"
    "sort"
)

func generateIntegers(a, b int) []int {
    var evenDigits []int
    for i := a; i <= b; i++ {
        str := fmt.Sprintf("%d", i)
        for j := 0; j < len(str); j++ {
            if str[j]%2 == 0 {
                evenDigits = append(evenDigits, i)
                break
            }
        }
    }
    sort.Ints(evenDigits)
    return evenDigits
}

func main() {
    fmt.Println(generateIntegers(2, 8))  // [2, 4, 6, 8]
    fmt.Println(generateIntegers(8, 2))  // [2, 4, 6, 8]
    fmt.Println(generateIntegers(10, 14)) // []
}
```

Solution:
```go
package main

import (
    "fmt"
    "sort"
)

func generateIntegers(a, b int) []int {
    var evenDigits []int
    for i := a; i <= b; i++ {
        str := fmt.Sprintf("%d", i)
        for j := 0; j < len(str); j++ {
            if str[j] >= '0' && str[j] <= '9' && str[j]%2 == 0 {
                evenDigits = append(evenDigits, i)
            }
        }
    }
    sort.Ints(evenDigits)
    return evenDigits
}

func main() {
    fmt.Println(generateIntegers(2, 8))  // [2, 4, 6, 8]
    fmt.Println(generateIntegers(8, 2))  // [2, 4, 6, 8]
    fmt.Println(generateIntegers(10, 14)) // []
}
```

Explanation:

1.  The function `generateIntegers` takes two positive integers `a` and `b` as input and returns a slice of even digits between `a` and `b`, in ascending order.
2.  The function uses two nested loops to iterate over the digits of each integer in the range `[a, b]`.
3.  The outer loop iterates over the integers in the range `[a, b]`.
4.  The inner loop iterates over the digits of each integer. It checks if the