return countNumbersWithOneDigit(n)
}

func countNumbersWithOneDigit(n int) int {
    if n == 1 {
        return 9
    }
    if n == 2 {
        return 90
    }
    return 9 * 9 + 9 * (n - 1) * 10 + 9 * 10 + 1
}

package main
import (
    "fmt"
    "math"
)

func main() {
    fmt.Println(StartsOneEnds(3)) // Output: 270
    fmt.Println(StartsOneEnds(2)) // Output: 90
    fmt.Println(StartsOneEnds(1)) // Output: 9
}