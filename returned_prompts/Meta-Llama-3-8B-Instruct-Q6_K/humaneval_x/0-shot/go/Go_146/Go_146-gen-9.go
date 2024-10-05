Here is the solution in Go:

```go
package main

import (
    "fmt"
    "strconv"
)

func Specialfilter(nums []int) int {
    var count int
    for _, num := range nums {
        if num > 10 && isOddFirstAndLast(strconv.Itoa(num)) {
            count++
        }
    }
    return count
}

func isOddFirstAndLast(s string) bool {
    firstDigit, _ := strconv.Atoi(string(s[0]))
    lastDigit, _ := strconv.Atoi(string(s[len(s)-1]))
    return firstDigit%2 != 0 && lastDigit%2 != 0
}

func main() {
    fmt.Println(Specialfilter([]int{15, -73, 14, -15})) // 1
    fmt.Println(Specialfilter([]int{33, -2, -3, 45, 21, 109})) // 2
}
```

This program defines a function `Specialfilter` that takes a slice of integers as input and returns the count of elements that are greater than 10 and have both the first and last digits as odd numbers.

The `isOddFirstAndLast` function is used to check if a number is odd by converting it to a string, extracting the first and last digits, and checking if they are odd using the modulus operator.

In the `main` function, we test the `Specialfilter` function with the provided examples. The output will be the expected results.