    return int(math.Pow(2, float64(n-1)))
}

// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that start and end with 1.
func StartsEndsOne(n int) int {

B:
    return int(math.Pow(2, float64(n-1)))
}

// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that start with 1 and end with any other digit.
func StartsOneEndsAny(n int) int {

C:
    return int(math.Pow(2, float64(n-1))) * 9
}

// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that start with 1 and end with any other digit.
func StartsOneEndsAnyExceptOne(n int) int {

D:
    return int(math.Pow(2, float64(n-1))) * 8
}
```

## Test Cases

```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println(StartsOneEnds(1)) // 2
    fmt.Println(StartsOneEnds(2)) // 4
    fmt.Println(StartsOneEnds(3)) // 8
    
    fmt.Println(StartsEndsOne(1)) // 2
    fmt.Println(StartsEndsOne(2)) // 4
    fmt.Println(StartsEndsOne(3)) // 8
    
    fmt.Println(StartsOneEndsAny(1)) // 18
    fmt.Println(StartsOneEndsAny(2)) // 36
    fmt.Println(StartsOneEndsAny(3)) // 72
    
    fmt.Println(StartsOneEndsAnyExceptOne(1)) // 10
    fmt.Println(StartsOneEndsAnyExceptOne(2)) // 20
    fmt.Println