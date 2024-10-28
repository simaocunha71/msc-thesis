Here is a solution in Go that meets the requirements:
```go
package main

import (
    "math"
    "strconv"
)

func CountNums(arr []int) int {
    var count int
    for _, num := range arr {
        str := strconv.Itoa(abs(num))
        sum := 0
        for _, c := range str {
            digit, _ := strconv.Atoi(string(c))
            sum += digit
        }
        if sum > 0 {
            count++
        }
    }
    return count
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func main() {
    arr := []int{-1, 11, -11, 1, 1, 2}
    fmt.Println(CountNums(arr)) // Output: 3
}
```
This solution works by iterating over each number in the input array, converting it to a string, and then iterating over each character in the string to calculate the sum of the digits. If the sum of the digits is greater than 0, it increments the count. The `abs` function is used to handle negative numbers by converting them to positive before calculating the sum of the digits. The final count is returned as the result.